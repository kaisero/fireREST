"""Auto-generate API reference pages from the fireREST.fmc package at build time.

Called by the mkdocs-gen-files plugin during `mkdocs build`.
Scans fireREST/fmc/ for all Resource/ChildResource/NestedChildResource subclasses
and writes one reference page per top-level namespace into the virtual docs tree.
"""
import ast
from pathlib import Path

import mkdocs_gen_files

BASE = Path('fireREST/fmc')
RESOURCE_BASES = {'Resource', 'ChildResource', 'NestedChildResource'}

NS_LABELS: dict[str, str] = {
    'analysis': 'Analysis',
    'assignment': 'Assignment',
    'audit': 'Audit',
    'backup': 'Backup',
    'changemanagement': 'Change Management',
    'chassis': 'Chassis',
    'deployment': 'Deployment',
    'device': 'Device',
    'devicecluster': 'Device Cluster',
    'devicegroup': 'Device Group',
    'devicehapair': 'Device HA Pair',
    'health': 'Health',
    'integration': 'Integration',
    'intelligence': 'Intelligence',
    'job': 'Job',
    'license': 'License',
    'netmap': 'NetMap',
    'object': 'Object',
    'policy': 'Policy',
    'system': 'System',
    'systemconfiguration': 'System Configuration',
    'troubleshoot': 'Troubleshoot',
    'update': 'Update',
    'user': 'User',
}

CLASS_OPTIONS = '''\
    options:
      show_root_heading: true
      heading_level: 2
      show_source: false
      show_bases: true
      inherited_members: true
      filters:
        - "!^_"
'''


def resource_class_name(path: Path) -> str | None:
    """Return the first Resource subclass name in *path*, or None."""
    try:
        tree = ast.parse(path.read_text(encoding='utf-8'))
    except (SyntaxError, OSError):
        return None
    for node in ast.walk(tree):
        if not isinstance(node, ast.ClassDef):
            continue
        for base in node.bases:
            if (isinstance(base, ast.Name) and base.id in RESOURCE_BASES) or (
                isinstance(base, ast.Attribute) and base.attr in RESOURCE_BASES
            ):
                return node.name
    return None


def to_module(init_file: Path) -> str:
    """Convert fireREST/fmc/object/network/__init__.py → fireREST.fmc.object.network"""
    return '.'.join(p for p in init_file.with_suffix('').parts if p != '__init__')


nav = mkdocs_gen_files.Nav()

# ── Home (keep in generated nav so literate-nav owns the full nav) ─────────
nav['Home'] = 'index.md'

# ── FMC client page ────────────────────────────────────────────────────────
with mkdocs_gen_files.open('reference/fmc.md', 'w') as fh:
    fh.write('# FMC Client\n\n')
    fh.write('::: fireREST.fmc.Connection\n')
    fh.write(CLASS_OPTIONS)

nav['API Reference', 'FMC Client'] = 'reference/fmc.md'

# ── One page per top-level namespace ──────────────────────────────────────
for ns_dir in sorted(BASE.iterdir()):
    if not ns_dir.is_dir() or ns_dir.name.startswith('_'):
        continue

    ns = ns_dir.name
    label = NS_LABELS.get(ns, ns.title())
    page = f'reference/{ns}.md'

    directives: list[str] = []
    for init_file in sorted(ns_dir.rglob('__init__.py')):
        cls = resource_class_name(init_file)
        if cls is None:
            continue
        mod = to_module(init_file)
        directives.append(f'::: {mod}.{cls}\n{CLASS_OPTIONS}')

    if not directives:
        continue

    with mkdocs_gen_files.open(page, 'w') as fh:
        fh.write(f'# {label}\n\n')
        fh.write('\n'.join(directives))

    nav['API Reference', label] = page

# ── Write SUMMARY.md consumed by literate-nav ─────────────────────────────
with mkdocs_gen_files.open('SUMMARY.md', 'w') as fh:
    fh.writelines(nav.build_literate_nav())
