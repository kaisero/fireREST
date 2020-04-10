[![python3](https://img.shields.io/badge/python-3.7+-blue.svg)](https://github.com/kaisero/fireREST/) [![pypi](https://img.shields.io/pypi/v/fireREST)](https://pypi.org/project/fireREST/) [![license](https://img.shields.io/badge/license-GPL%20v3.0-brightgreen.svg)](https://github.com/kaisero/fireREST/blob/master/LICENSE) [![status](https://img.shields.io/badge/status-alpha-blue.svg)](https://github.com/kaisero/fireREST/) [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/kaisero/fireREST)


# FireREST

A simple wrapper for firepower management center restful api.

## Features

* Authentication and automatic session refresh
* Rate-limit handling with automatic retry operation
* Automatic squashing of paginated api payloads
* Sanitization of api payloads received via GET operations and used for PUT/POST operations
* Debug logging for api calls using logger module
* Result caching for various operations

## Requirements

* Python >= 3.7

## Quickstart

### Installation

```bash
pip install fireREST
```

### Import api client

```python
from fireREST import Client
```

### Authentication

FireREST uses basic authentication to authenticate with fmc. You may also provide a session dictionary
to re-use an existing authentication token. In case your authentication token times out the api client
will automatically try to re-authenticate 3 times and handle any intermediate authentication exceptions.

#### Basic Authentication

```python
client = Client(hostname='fmc.example.com', username='firerest', password='Cisco123')
```

#### Re-using an existing session

```python
auth_session = {
  'X-auth-access-token': 'c26c28a0-c871-454f-b8e0-18c60c00562e',
  'X-auth-refresh-token': '9d381948-2fde-47d0-a28b-f4b0bb21fe81',
  'DOMAINS': '[{"name":"Global","uuid":"e276abec-e0f2-11e3-8169-6d9ed49b625f"}, {"name":"Global/Devel","uuid":"61e913a3-4bd6-7bde-54b6-000000000000"}]',
}
client = Client(hostname='fmc.example.com', session=auth_session)
```

### Helper

A variety of helper functions can be used to translate object names to their respective UUID values. Since fmc rest api uses uuid values this is neccessary
to find pre-existing objects by the name defined in fmc.

#### Object Name to ID

```python
name = 'NET_OBJ'
uuid = client.get_object_id_by_name('network', name)
```

#### Access Control Policy Name to ID

```python
name = 'DEV-ACCESS-CONTROL-POLICY'
uuid = client.get_acp_id_by_name(name)
```

#### Access Control Policy Rule Name to ID

```python
acp = 'DEV-ACCESS-CONTROL-POLICY'
acp_rule = 'PERMIT-INTERNET-ACCESS'
uuid = client.get_object_id_by_name(acp, acp_rule)
```

### Objects

#### Create Network Object

```python
net_obj = {
    'name': 'NetObjViaAPI',
    'value': '198.18.1.0/24',
}

response = client.create_object('network', net_obj)
```

#### Get Network Object

```python
obj_name = 'NetObjViaAPI'
obj_id = client.get_object_id_by_name('network', 'NetObjViaAPI')
obj_payload = client.get_object('network', obj_id)
```

#### Update Network Object

```python
obj_name = 'NetObjViaAPI'
obj_id = client.get_object_id_by_name('network', 'NetObjViaAPI')

net_obj = {
    'id': obj_id,
    'name': 'NetObjViaAPI',
    'value': '198.18.2.0/24',
}

response = client.update_object('network', obj_id, net_obj)
```

#### Delete Network Object

```python
obj_name = 'NetObjViaAPI'
obj_id = client.get_object_id_by_name('network', 'NetObjViaAPI')
response = client.delete_object('network', obj_id)
```


## Authors

Oliver Kaiser (oliver.kaiser@outlook.com)

## License

GNU General Public License v3.0 or later.

See [LICENSE](LICENSE) for the full text.
