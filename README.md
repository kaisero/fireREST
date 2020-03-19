# What is FireREST

FireREST is a simple wrapper for Cisco Firepower Management Center REST API. It exposes various api calls
as functions and takes care of authentication, token refresh and paging for large datasets.

## Requirements 

* Python >= 3.7

## Installation

```bash
$ pip install fireREST
```

## Usage

### Import API Client

```python
from fireREST import Client
```

### Authentication

FireREST uses basic authentication to authenticate to FMC. You may also provide a session dictionary
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

A variety of helper functions can be used to translate object names to their respective UUID values. Since FMC REST API uses UUID values this is neccessary
to find pre-existing objects by the name defined in FMC UI.

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
policy_name = 'DEV-ACCESS-CONTROL-POLICY'
rule_name = 'PERMIT-INTERNET-ACCESS'
uuid = client.get_object_id_by_name(policy_name, rule_name)
```

### Objects

#### Create Network Object

```python
net_obj = { 
    'name': 'NetObjViaAPI',
    'value': '198.18.1.0/24',
}

response = client.create_object('networks', net_obj)
```

#### Get Network Object

```python
obj_name = 'NetObjViaAPI'
obj_id = client.get_object_id_by_name('networks', 'NetObjViaAPI')
obj_payload = client.get_object('networks', obj_id)[0].json()
```

Note: FireREST always return a list of requests responses, even if a single item is retrieved. This
was an intentional decision to make handling of api responses consistent

#### Update Network Object

```python
obj_name = 'NetObjViaAPI'
obj_id = client.get_object_id_by_name('networks', 'NetObjViaAPI')

net_obj = {
    'id': obj_id,
    'name': 'NetObjViaAPI',
    'value': '198.18.2.0/24',
}

response = client.update_object('networks', obj_id, net_obj)
```

#### Delete Network Object

```python
obj_name = 'NetObjViaAPI
obj_id = client.get_object_id_by_name('networks', 'NetObjViaAPI')
response = client.delete_object('networks', obj_id)
```


## Authors 

Oliver Kaiser (oliver.kaiser@outlook.com)

## License

GNU General Public License v3.0
