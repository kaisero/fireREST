"""Generate Google-style docstrings for all fireREST resource classes from OAS3 specs."""

import ast
import json
import re
import sys
from pathlib import Path

# ── Namespace → OAS3 base-path prefix ────────────────────────────────────────
NAMESPACE_PREFIXES = {
    'config': '/api/fmc_config/v1/domain/{domainUUID}',
    'platform': '/api/fmc_platform/v1',
    'platform_with_domain': '/api/fmc_platform/v1/domain/{domainUUID}',
    'netmap': '/api/fmc_netmap/v1/domain/{domainUUID}',
    'tid': '/api/fmc_tid/v1',
    'troubleshoot': '/api/fmc_troubleshoot/v1/domain/{domainUUID}',
    'base': '',
}

# Parameters managed internally by the library — omit from generated docstrings
SKIP_PARAMS = {
    'domainUUID', 'objectId', 'containerUUID', 'childContainerUUID',
    'targetId', 'domainID', 'ticket-id',
}

# Resolved values for $ref parameters
REF_PARAMS = {
    'offset':   {'name': 'offset',   'type': 'integer', 'desc': 'Index of first item to return.'},
    'limit':    {'name': 'limit',    'type': 'integer', 'desc': 'Number of items to return.'},
    'expanded': {'name': 'expanded', 'type': 'boolean', 'desc': 'Include extended sub-object details in response.'},
}


def normalize_path(path: str) -> str:
    return re.sub(r'\{[^}]+\}', '{p}', path)


def clean_desc(text: str) -> str:
    text = text.strip()
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text, flags=re.DOTALL)
    text = re.sub(r'_(.+?)_', r'\1', text, flags=re.DOTALL)
    text = re.sub(r'<code>(.+?)</code>', r'`\1`', text)
    text = re.sub(r'<br\s*/?>', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    # Trim trailing "Check the response section..." boilerplate
    text = re.sub(r'\s*Check the response section.*$', '', text, flags=re.IGNORECASE).strip()
    return text


def load_specs() -> dict:
    """Load all three OAS3 JSON files; newest version takes precedence."""
    combined: dict = {}
    for fname in ['.llm/fmc_oas3_7.2.5.json', '.llm/fmc_oas3_7.3.1.json', '.llm/fmc_oas3_7.4.2.json']:
        p = Path(fname)
        if p.exists():
            with p.open(encoding='utf-8') as f:
                spec = json.load(f)
            combined.update(spec.get('paths', {}))
    return combined


def build_lookup(paths: dict) -> dict:
    """normalized_path → {original_path, methods}"""
    lookup: dict = {}
    for path, methods in paths.items():
        norm = normalize_path(path)
        lookup[norm] = {'original_path': path, 'methods': methods}
    return lookup


def find_ops(class_path: str, namespace: str, lookup: dict) -> dict:
    """
    Return ops dict with keys: GET, GET_LIST, POST, PUT, PUT_BULK, DELETE, DELETE_LIST.
    Values are the raw OAS3 operation dicts.
    """
    prefix = NAMESPACE_PREFIXES.get(namespace, NAMESPACE_PREFIXES['config'])
    full = prefix + class_path
    collection = re.sub(r'/\{[^}]+\}$', '', full)

    norm_full = normalize_path(full)
    norm_coll = normalize_path(collection)

    ops: dict = {}

    # Single-object path (GET, PUT, DELETE on /{uuid})
    if norm_full != norm_coll and norm_full in lookup:
        for method, op in lookup[norm_full]['methods'].items():
            ops[method.upper()] = op

    # Collection path (GET list, POST, sometimes PUT bulk / DELETE bulk)
    if norm_coll in lookup:
        for method, op in lookup[norm_coll]['methods'].items():
            key = method.upper()
            if key == 'GET':
                ops['GET_LIST'] = op
            elif key == 'PUT':
                ops['PUT_BULK'] = op if 'PUT' in ops else ops.setdefault('PUT', op)
            elif key == 'DELETE':
                ops['DELETE_LIST'] = op if 'DELETE' in ops else ops.setdefault('DELETE', op)
            else:
                ops.setdefault(key, op)

    return ops


def collect_query_params(ops: dict) -> list:
    """Collect unique query parameters across all operations, resolved and deduped."""
    seen: set = set()
    result: list = []

    for op in ops.values():
        for param in op.get('parameters', []):
            if '$ref' in param:
                ref_name = param['$ref'].split('/')[-1]
                if ref_name in REF_PARAMS and ref_name not in seen:
                    seen.add(ref_name)
                    r = REF_PARAMS[ref_name]
                    result.append({'name': r['name'], 'type': r['type'],
                                   'desc': r['desc'], 'required': False})
                continue

            name = param.get('name', '')
            if name in SKIP_PARAMS or name in seen:
                continue
            if param.get('in') != 'query':
                continue

            seen.add(name)
            p_type = param.get('schema', {}).get('type', 'str')
            p_desc = clean_desc(param.get('description', ''))
            p_req = param.get('required', False)
            result.append({'name': name, 'type': p_type, 'desc': p_desc, 'required': p_req})

    return result


def make_docstring(ops: dict) -> list[str] | None:
    """Return raw docstring lines (no indentation) or None if nothing to write."""
    if not ops:
        return None

    # Best description: prefer GET single, then GET_LIST, then any
    desc = ''
    for key in ('GET', 'GET_LIST', 'POST', 'PUT', 'DELETE'):
        if key in ops:
            raw = ops[key].get('description', '')
            if raw:
                desc = clean_desc(raw)
                break
    if not desc:
        return None

    # Tags (deduplicated, preserve order)
    tags: list = []
    for op in ops.values():
        for t in op.get('tags', []):
            if t not in tags:
                tags.append(t)

    # Supported CRUD (deduplicate GET)
    crud_order = [('GET', 'GET'), ('GET_LIST', 'GET'), ('POST', 'CREATE'),
                  ('PUT', 'UPDATE'), ('PUT_BULK', 'UPDATE'), ('DELETE', 'DELETE'), ('DELETE_LIST', 'DELETE')]
    supported: list = []
    for key, label in crud_order:
        if key in ops and label not in supported:
            supported.append(label)

    # Operation IDs
    op_id_order = [
        ('GET_LIST', 'GET (list)'), ('GET', 'GET'),
        ('POST', 'CREATE'), ('PUT_BULK', 'UPDATE (bulk)'), ('PUT', 'UPDATE'),
        ('DELETE_LIST', 'DELETE (bulk)'), ('DELETE', 'DELETE'),
    ]
    op_ids: list = []
    for key, label in op_id_order:
        if key in ops:
            op_id = ops[key].get('operationId', '')
            if op_id:
                op_ids.append((label, op_id))

    # Query parameters
    query_params = collect_query_params(ops)

    # ── Build raw lines (no indentation yet) ─────────────────────────────────
    lines: list[str] = [f'"""{desc}', '']

    if tags:
        lines += [f'**Tags:** {", ".join(tags)}', '']

    if supported:
        lines += [f'**Supported operations:** {", ".join(supported)}', '']

    if op_ids:
        lines += ['**Operation IDs:**', '']
        for label, op_id in op_ids:
            lines.append(f'- `{op_id}` ({label})')
        lines.append('')

    if query_params:
        lines += ['**Query parameters:**', '']
        for p in query_params:
            opt = '' if p['required'] else ', optional'
            lines.append(f'- `{p["name"]}` ({p["type"]}{opt}): {p["desc"]}')
        lines.append('')

    # Trim trailing blank lines, add closing quotes
    while lines and lines[-1] == '':
        lines.pop()
    lines.append('"""')

    return lines


def extract_class_info(content: str):
    """Return (class_node, attrs, has_docstring) for the first Resource subclass in the file."""
    try:
        tree = ast.parse(content)
    except SyntaxError:
        return None, None, None

    for node in ast.walk(tree):
        if not isinstance(node, ast.ClassDef):
            continue

        # Must subclass Resource / ChildResource / NestedChildResource
        resource_bases = {'Resource', 'ChildResource', 'NestedChildResource'}
        is_resource = any(
            (isinstance(b, ast.Name) and b.id in resource_bases) or
            (isinstance(b, ast.Attribute) and b.attr in resource_bases)
            for b in node.bases
        )
        if not is_resource:
            continue

        attrs: dict = {}
        for item in node.body:
            if not isinstance(item, ast.Assign):
                continue
            for target in item.targets:
                if isinstance(target, ast.Name) and isinstance(item.value, ast.Constant):
                    name = target.id
                    if name in ('PATH', 'NAMESPACE'):
                        attrs[name] = item.value.value

        if 'PATH' not in attrs:
            continue

        has_docstring = (
            node.body and
            isinstance(node.body[0], ast.Expr) and
            isinstance(node.body[0].value, ast.Constant) and
            isinstance(node.body[0].value.value, str)
        )

        return node, attrs, has_docstring

    return None, None, None


def insert_docstring(filepath: str, class_node, raw_lines: list[str], indent: str = '    ') -> None:
    """Insert docstring as first statement of class body, with correct indentation."""
    with open(filepath, encoding='utf-8') as f:
        lines = f.readlines()

    insert_at = class_node.body[0].lineno - 1  # 0-indexed

    doc_lines: list[str] = []
    for line in raw_lines:
        doc_lines.append((indent + line + '\n') if line else '\n')

    lines = lines[:insert_at] + doc_lines + lines[insert_at:]

    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        f.writelines(lines)


def main():
    sys.stdout.reconfigure(encoding='utf-8')

    base = Path('fireREST/fmc')
    print('Loading OAS3 specs ...')
    oas3 = load_specs()
    lookup = build_lookup(oas3)
    print(f'  {len(oas3)} OAS3 paths loaded from 3 spec files')

    ok = skipped_match = skipped_existing = errors = 0

    for init_file in sorted(base.rglob('*/__init__.py')):
        # Skip the top-level fmc/__init__.py (the Connection class)
        if init_file.parent == base:
            continue
        try:
            content = init_file.read_text(encoding='utf-8')
            class_node, attrs, has_doc = extract_class_info(content)
            if class_node is None:
                continue
            if has_doc:
                skipped_existing += 1
                continue

            namespace = attrs.get('NAMESPACE', 'config')
            ops = find_ops(attrs['PATH'], namespace, lookup)

            if not ops:
                skipped_match += 1
                continue

            doc_lines = make_docstring(ops)
            if not doc_lines:
                skipped_match += 1
                continue

            insert_docstring(str(init_file), class_node, doc_lines)
            ok += 1
            print(f'  OK  {init_file}')

        except Exception as exc:
            errors += 1
            print(f'  ERR {init_file}: {exc}')

    print(f'\nDone — {ok} written, {skipped_existing} already had docstrings, '
          f'{skipped_match} no OAS3 match, {errors} errors')


if __name__ == '__main__':
    main()
