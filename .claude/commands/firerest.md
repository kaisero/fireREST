# fireREST Project Context

You are working on **fireREST** — a Python SDK for the Cisco Firepower Management Center (FMC) REST API.
Current version: **1.3.0**. Active branch: `feature/full_support_7.4`.
Maintainer on this fork: Christian Mendez (`cromanme/fireREST` on GitHub, upstream is `kaisero/fireREST`).

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

---

## Known Bugs (tracked in `.llm/fireREST_phase2_reference.md` §2)

| ID | File | Issue |
|---|---|---|
| BUG-01 | `netmap/host`, `netmap/vulnerability` | `delete()` passes `url=` kwarg — TypeError at runtime |
| BUG-02 | `devicecluster/ftddevicecluster/operational` | `command()` uses un-formatted `{container_uuid}` literal |
| BUG-03 | `chassis/operational` | 3 methods leave `{uuid}` un-substituted |
| BUG-04 | `health/tunnelsummary` | `PATH` uses metric's path, should be `/health/tunnelsummaries/{uuid}` |
| BUG-05 | `policy/networkanalysispolicy/inspectorconfig` | `CONTAINER_PATH` points to `intrusionpolicies` instead of `networkanalysispolicies` |
| BUG-06 | `policy/prefilterpolicy/defaultaction` | `CONTAINER_NAME = 'AccessPolicy'` should be `'PrefilterPolicy'` |
| BUG-07 | `policy/ftds2svpn/endpoint` | `CONTAINER_NAME = 'Endpoint'` should be `'FtdS2sVpn'` |
| BUG-08 | `policy/prefilterpolicy` | Attribute `accessrule` should be `prefilterrule` |
| BUG-09 | `deployment` | Attribute `deployabledevices` (plural) should be `deployabledevice` |
| BUG-10 | `mapping.py` | `PARAMS` missing `group_dependency` and `hostname` → KeyError |
| BUG-11 | `mapping.py` | `command` filter built ad-hoc in device operational, inconsistent |

Check `.llm/fireREST_phase2_reference.md` for exact fix snippets.

## Missing Implementations (`.llm/fireREST_phase2_reference.md` §3)

| ID | Issue |
|---|---|
| MISSING-01 | `policy.accesspolicy.loggingsettings` module exists but never instantiated in `AccessPolicy.__init__()` |
| MISSING-02 | `policy.identitypolicy` module exists but never wired into `Policy.__init__()` |
| MISSING-03 | `object.standardaccesslist` only has GET; CHANGELOG claimed create/update/delete |
| MISSING-04 | `VirtualRouter` missing `ospfv3route` and `ospfv3interface` subresources (no files exist) |
| MISSING-05 | `object.communitylist` only has GET; FMC API supports CREATE/UPDATE/DELETE |

---

## Documentation (MkDocs)

- Config: `mkdocs.yml` with Material theme, dark/light toggle, mkdocstrings
- Source: `docs/` — `index.md` (home) + `reference/*.md` (25 API reference pages)
- Each reference page uses explicit `:::` directives per class with `inherited_members: true`
- Build: `poetry run mkdocs build --strict`
- Sphinx was fully removed (no RST files remain)

---

## Development Workflow

```bash
# Install dev deps
poetry install

# Lint / format
poetry run pre-commit run --all-files

# Type check
poetry run mypy fireREST

# Tests
poetry run pytest --cov=fireREST --cov-report=term

# Build docs
poetry run mkdocs build --strict

# Build package
python -m build

# Publish to PyPI (kaisero granted access)
twine check dist/* && twine upload dist/*

# Tox (all environments)
tox
```

---

## URL Path Verification Checklist

Before adding any new resource, verify the exact API path in FMC API Explorer (`https://<fmc_ip>/api/api-explorer`) or the OAS3 specs in `.llm/`:
1. Singular vs plural in path segment
2. `fmc_config` vs `fmc_platform` API
3. Whether a domain UUID is required
4. Which HTTP methods are supported
5. Supported filter/query parameters

OAS3 specs available:
- `.llm/fmc_oas3_7.2.5.json`
- `.llm/fmc_oas3_7.3.1.json`
- `.llm/fmc_oas3_7.4.2.json`
