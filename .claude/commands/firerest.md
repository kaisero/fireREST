# fireREST Project Context

You are working on **fireREST** — a Python SDK for the Cisco Firepower Management Center (FMC) REST API.
Current version: **1.3.0** (CHANGELOG header is `# Unreleased` until release is cut).
PyPI publish access granted by kaisero.

---

## Architecture

```
FMC (fireREST/__init__.py)
└── Connection (fireREST/fmc/__init__.py)   ← HTTP, auth, sessions, URL building
    ├── Resource                             ← top-level objects (no container)
    ├── ChildResource(Resource)             ← objects inside one container
    └── NestedChildResource(ChildResource)  ← objects inside a ChildResource
```

Every API resource is a class in `fireREST/fmc/<namespace>/<resource>/__init__.py`.
Parent namespace grouping classes (e.g. `Policy`, `Object`) live in `fireREST/fmc/<namespace>/__init__.py`
and only hold `__init__(self, conn)` that instantiates child resources as attributes.

### Key Decorators (`fireREST/utils.py`)
| Decorator | Purpose |
|---|---|
| `@utils.minimum_version_required` | Enforces FMC version floor per CRUD op |
| `@utils.resolve_by_name` | Auto-resolves `name` → `uuid` via GET-all |
| `@utils.support_params` | Builds `filter=key:val;...` and `?param=val` strings |
| `@utils.handle_errors` | HTTP error + rate-limit retry handler |

### URL Namespaces (set via `NAMESPACE` class attribute)
| Key | Base path |
|---|---|
| `config` *(default)* | `/api/fmc_config/v1/domain/{domainUUID}` |
| `platform` | `/api/fmc_platform/v1` |
| `platform_with_domain` | `/api/fmc_platform/v1/domain/{domainUUID}` |
| `netmap` | `/api/fmc_netmap/v1/domain/{domainUUID}` |
| `tid` | `/api/fmc_tid/v1` |
| `troubleshoot` | `/api/fmc_troubleshoot/v1/domain/{domainUUID}` |
| `base` | raw URL (no prefix) |

### PATH placeholder convention
- `{uuid}` — the resource itself
- `{container_uuid}` — the direct parent container
- `{child_container_uuid}` — the grandparent container (NestedChildResource only)

`fix_url()` strips trailing `/None`, so `uuid=None` → list endpoint automatically.

### API release constants (`fireREST/defaults.py`)
```python
API_RELEASE_600 … API_RELEASE_720   # pre-existing
API_RELEASE_730 = '7.3.0'
API_RELEASE_740 = '7.4.0'
API_RELEASE_760 = '7.6.0'
API_RELEASE_770 = '7.7.0'
API_RELEASE_1000 = '10.0.0'
```
Use `'99.99.99'` (the class default) for unsupported CRUD operations — do not omit the constant.

---

## Code Style Rules (enforced by ruff)
- **Single quotes** for all strings
- **120-character** line length max
- **Type hints**: `Optional[str]`, `Dict`, `Union[dict, list]`
- **Import order**: stdlib → third-party → local, sorted within groups
- All FMC API URL path segments use **plural nouns** (e.g. `/accessrules/`, `/networks/`)
- Always declare all four `MINIMUM_VERSION_REQUIRED_*` constants explicitly

---

## Code Templates

### Top-level Resource
```python
from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource

class MyResource(Resource):
    NAMESPACE = 'config'                        # change if not config API
    PATH = '/category/myresources/{uuid}'
    SUPPORTED_FILTERS: list[str] = []
    SUPPORTED_PARAMS: list[str] = []
    IGNORE_FOR_CREATE: list[str] = []
    IGNORE_FOR_UPDATE: list[str] = []
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET    = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_740
```

### ChildResource (one container)
```python
from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource

class MyChild(ChildResource):
    CONTAINER_NAME = 'ParentClass'
    CONTAINER_PATH = '/category/parents/{uuid}'
    PATH = '/category/parents/{container_uuid}/children/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
```

### NestedChildResource (two containers)
```python
from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import NestedChildResource

class MyNested(NestedChildResource):
    CONTAINER_NAME = 'GrandParentClass'
    CONTAINER_PATH = '/category/grandparents/{uuid}'
    CHILD_CONTAINER_NAME = 'ParentClass'
    CHILD_CONTAINER_PATH = '/category/grandparents/{container_uuid}/parents/{uuid}'
    PATH = '/category/grandparents/{container_uuid}/parents/{child_container_uuid}/children/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
```

### Namespace grouping class
```python
from fireREST.fmc import Connection
from fireREST.fmc.mynewsection.myresource import MyResource

class MySection:
    def __init__(self, conn: Connection):
        self.myresource = MyResource(conn)
```

Wire into FMC root (`fireREST/__init__.py`):
```python
from fireREST.fmc.mynewsection import MySection
# inside FMC.__init__:
self.mynewsection = MySection(self.conn)
```

### Adding filter/param support
1. Add `SUPPORTED_FILTERS` or `SUPPORTED_PARAMS` list to the class.
2. Add the snake_case → camelCase mapping to `fireREST/mapping.py` in `FILTERS` or `PARAMS`.
3. Write a custom `get()` decorated with `@utils.support_params`.

### Docstring format (all 312 resource classes already have these)
Generated from OAS3 specs via `gen_docstrings.py`. Format:
```python
"""<description from OAS3 GET operation>.

**Tags:** Object

**Supported operations:** GET, CREATE, UPDATE, DELETE

**Operation IDs:**

- `getAllNetworkObject` (GET (list))
- `getNetworkObject` (GET)
- `createMultipleNetworkObject` (CREATE)
- `updateNetworkObject` (UPDATE)
- `deleteNetworkObject` (DELETE)

**Query parameters:**

- `filter` (string, optional): Filter by name or value.
- `expanded` (boolean, optional): Include extended sub-object details in response.
- `offset` (integer, optional): Index of first item to return.
- `limit` (integer, optional): Number of items to return.
"""
```
To regenerate docstrings after adding new classes: `python gen_docstrings.py`

---

## PR Review — rchrabas Preferences (upstream collaborator)

rchrabas reviews all PRs against `kaisero/fireREST`. Known preferences:
- **Breaking changes** must be in a separate `## Breaking Changes` section in CHANGELOG — not buried in `## Fixed`.
- **Renames of public attributes** (e.g. `deployabledevices` → `deployabledevice`) are breaking changes. If rchrabas pushes back on a rename, revert it and leave the old name.
- **CHANGELOG header** should be `# Unreleased` while the PR is open; versioned only after merge.
- **Publishing** is done manually via `uv build && uv publish` — do not automate in CI without approval.
- **pyproject.toml** classifiers: Python 3.9 is EoL, omit it. Start from 3.10.
- **Docs reference pages** must be auto-generated from code, not static committed files.
- **CHANGELOG bug descriptions**: keep to one concise line each — no multi-line "because..." explanations.
- **gh CLI** is installed at `C:\Program Files\GitHub CLI\gh.exe` (not on PATH in Bash tool — use PowerShell or full path).

---

## Known Bugs — ALL FIXED on `feature/full_support_7.4`

BUG-01 through BUG-11 from `.llm/fireREST_phase2_reference.md` §2 are resolved.
Note: BUG-09 (`deployabledevices` rename) was **reverted** at rchrabas's request — attribute stays plural.

## Missing Implementations — ALL FIXED on `feature/full_support_7.4`

MISSING-01 through MISSING-05 from `.llm/fireREST_phase2_reference.md` §3 are resolved.

---

## Documentation (MkDocs)

- Config: `mkdocs.yml` — Material theme, dark/light toggle, mkdocstrings, gen-files, literate-nav
- Home page: `docs/index.md` (static)
- Reference pages: **auto-generated at build time** by `docs/gen_ref_pages.py`
  - Scans `fireREST/fmc/` via AST, emits one page per namespace with `:::` directives
  - Navigation auto-populated via `SUMMARY.md` written by literate-nav
  - Adding a new resource class → appears in docs automatically on next build
- Build: `make docs` or `uv run --group docs mkdocs build --strict`
- Local preview: `uv run --group docs mkdocs serve` → `http://127.0.0.1:8000`
- Sphinx fully removed (no RST files remain)
- Dev deps in `[dependency-groups] docs` in `pyproject.toml`

### CHANGELOG format
```markdown
# Unreleased         ← always "Unreleased" while PR is open

## New
* ...

## Documentation
* ...

## Breaking Changes
* ...

## Fixed
* Fixed <short one-line description>.
```

---

## Development Workflow

```bash
# Install all dev + docs deps
uv sync --group dev --group docs

# Lint / format
make pre-commit

# Type check
make mypy

# Tests
make test

# Build docs (local preview)
uv run --group docs mkdocs serve

# Build docs (static output to site/)
make docs

# Build package
make build   # or: uv build

# Run all checks (pre-commit, mypy, test, docs, build)
make check

# Publish to PyPI (kaisero granted access — do manually)
uv publish

# Read PR comments
gh api repos/kaisero/fireREST/pulls/<N>/comments

# List PRs
gh pr list --repo kaisero/fireREST --state all
```

---

## URL Path Verification Checklist

Before adding any new resource, verify the exact API path in FMC API Explorer (`https://<fmc_ip>/api/api-explorer`) or the OAS3 specs in `.llm/`:
1. Singular vs plural in path segment
2. `fmc_config` vs `fmc_platform` API
3. Whether a domain UUID is required
4. Which HTTP methods are supported
5. Supported filter/query parameters
6. Whether the endpoint has an individual `/{uuid}` path or is list-only — if list-only, omit `/{uuid}` from PATH

OAS3 specs available:
- `.llm/fmc_oas3_7.2.5.json`
- `.llm/fmc_oas3_7.3.1.json`
- `.llm/fmc_oas3_7.4.2.json`

---

## Audit-Derived Rules (from `AUDIT_REPORT.md`, branch `code-audit`, June 2026)

### TID Namespace URL
The `'tid'` namespace URL builder in `fireREST/fmc/__init__.py` is **missing** the `/domain/{domainUUID}` segment. Current form produces `/api/fmc_tid/v1{path}`; correct form is `/api/fmc_tid/v1/domain/{domain_id}{path}`. All TID resources return 404 until this is fixed (C-02).

### SUPPORTED_FILTERS / SUPPORTED_PARAMS validation
Every key in `SUPPORTED_FILTERS` **must** appear in `FILTERS` dict in `fireREST/mapping.py`. Every key in `SUPPORTED_PARAMS` **must** appear in `PARAMS` dict. A missing entry causes a `KeyError` at runtime when the user supplies that kwarg. Also watch for:
- Keys that belong in `SUPPORTED_FILTERS` accidentally placed in `SUPPORTED_PARAMS` (e.g., `operation`, `section`)
- Keys that belong in `SUPPORTED_PARAMS` accidentally in `SUPPORTED_FILTERS` (e.g., `section` in NatRule)

### /{uuid} suffix on list-only endpoints
Many fireREST classes append `/{uuid}` to paths that the OAS3 spec only defines as list endpoints. `fix_url()` strips trailing `/None` so list calls work, but any call with a UUID generates a 404. When the spec has no individual-item path, **omit `/{uuid}` from PATH**. Affected resources found in audit: AllowDnsRule, BlockDnsRule, Hitcount (both), PreviewChanges, ValidationResults, DownloadReport, EmailReport, FpInterfaceStatistics, ManagementConvergenceMode, AppInfo.

### IpsecCryptoMap container
`IpsecCryptoMap` belongs under `RaVpn` container (`/policy/ravpns/`), NOT `FtdS2sVpn`. The `ftds2svpns` container has no `ipseccryptomaps` endpoint in any spec version.

### S2sVpnSummary
The `/policy/s2svpnsummaries` endpoint is a top-level `Resource`, not a child of `FtdS2sVpn`. The current `S2sVpnSummary` ChildResource under `FtdS2sVpn` uses a path that does not exist in the spec.

### Known no-ops (unmerged fix)
`Hitcount.update()` and `Hitcount.delete()` in both AccessPolicy and PrefilterPolicy Hitcount classes `return` without making any HTTP call. Fix is on branch `fix/102-hitcount-delete` (Issue #102), not yet merged to master.

### Deprecated resources
`health/csdac` (`PATH = '/health/csdac/{uuid}'`) is not present in OAS3 7.4.2 — the endpoint was removed from FMC API.
