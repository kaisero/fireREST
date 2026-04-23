[![python3](https://img.shields.io/badge/python-3.9+-blue.svg)](https://github.com/kaisero/fireREST/)
[![pypi](https://img.shields.io/pypi/v/fireREST)](https://pypi.org/project/fireREST/)
[![license](https://img.shields.io/badge/license-GPL%20v3.0-brightgreen.svg)](https://github.com/kaisero/fireREST/blob/master/LICENSE)

# FireREST

FireREST is a Python library for interfacing with the Cisco Firepower Management Center (FMC) REST API. It provides a simple SDK to programmatically interact with FMC up to version **7.4.0**.

## Features

- Authentication and automatic session refresh / re-authentication
- Rate-limit detection and automatic backoff and retry behavior
- Automatic squashing of paginated API payloads
- Sanitization of API payloads for create and update operations
- Detailed logging of API requests and responses
- API-specific error handling with custom exceptions
- Resource lookup by name instead of UUID for all CRUD operations
- Support for Cloud Delivered FMC (cdFMC / CDO)

## Installation

```bash
pip install fireREST
```

## Authentication

### Self-hosted FMC

```python
from fireREST import FMC

fmc = FMC(hostname='fmc.example.com', username='firerest', password='Cisco123', domain='Global')
```

!!! note
    `domain` defaults to `Global` if not specified.

### Cloud Delivered FMC (cdFMC / CDO)

```python
fmc = FMC(hostname='example.app.eu.cdo.cisco.com', password='<CDO Token>', cdo=True)
```

## CRUD Operations

### Create a network object

```python
net_obj = {
    'name': 'NetObjViaAPI',
    'value': '198.18.1.0/24',
}
response = fmc.object.network.create(data=net_obj)
```

!!! note
    If a resource supports the `bulk` option, FireREST will automatically perform a bulk operation when `data` is a `list`.

### Get all network objects

```python
net_objects = fmc.object.network.get()
```

### Get a specific network object

```python
net_obj = fmc.object.network.get(name='NetObjViaAPI')
```

!!! note
    You can access a resource by `name` or `uuid`. FireREST uses API filter params when available, or iterates all resources to find a match.

### Update a network object

```python
net_obj = fmc.object.network.get(name='NetObjViaAPI')
net_obj['name'] = 'RenamedNetObjViaAPI'
response = fmc.object.network.update(data=net_obj)
```

!!! note
    FireREST automatically extracts the `id` field from the data dict to target the correct resource.

### Delete a network object

```python
response = fmc.object.network.delete(name='NetObjViaAPI')
```

## Troubleshooting

### UnprocessableEntityError

You may see `UnprocessableEntityError` on `CREATE` or `UPDATE` operations. If the FMC error message lacks detail, use `pigtail` on the FMC appliance:

```bash
expert
sudo su -
pigtail TCAT
```

Example output:

```
TCAT: 02-02 15:34:33 [ajp-nio-...] ERROR ... - **Invalid IP Address**
TCAT: 02-02 15:34:33 APIException:Invalid IP Address
```

## License

GNU General Public License v3.0 or later. See [LICENSE](https://github.com/kaisero/fireREST/blob/master/LICENSE).
