[![python3](https://img.shields.io/badge/python-3.7+-blue.svg)](https://github.com/kaisero/fireREST/) [![pypi](https://img.shields.io/pypi/v/fireREST)](https://pypi.org/project/fireREST/) [![license](https://img.shields.io/badge/license-GPL%20v3.0-brightgreen.svg)](https://github.com/kaisero/fireREST/blob/master/LICENSE) [![status](https://img.shields.io/badge/status-alpha-blue.svg)](https://github.com/kaisero/fireREST/) [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/kaisero/fireREST)


# FireREST

FireREST is a python library for Cisco Firepower Management Center. The goal of
FireREST is to provide a simple interface to interact with FMCs REST API without
much overhead.

## Features

* Authentication and automatic session refresh / re-authentication
* Rate-limit handling with automatic retry operations
* Automatic squashing of paginated api payloads
* Sanitization of api payloads for create and update operations
* Detailed logging of api calls

## Supported operations

Since FireREST does not try to provide a python object model nearly all api
calls up to version 6.7.0 are available which includes but is not limited to
the following CRUD operations:

* Devices
  * Interfaces
    * PhysicalInterfaces
    * RedundantInterfaces
    * EtherChannelInterfaces
    * SubInterfaces
    * VlanInterfaces
    * VirtualSwitches
    * InlineSets
    * VirtualTunnelInterfaces
  * Routing
    * StaticRoutes (IPv4 & IPv6)
    * VirtualRouters 
* DeviceHaPairs
* Objects
  * Hosts
  * Networks
  * NetworkGroups
  * Protocols
  * ProtocolGroups
  * URLs
  * UrlGroups
  * SecurityZones
* Policies
  * Accesspolicies
    * Accessrules
  * Prefilterpolicies
    * Prefilterrules
  * NatPolicies
    * ManualNatRules
    * AutoNatRules
* Deployment
  * DeployableDevices
  * Deploy
  * Rollback
  * JobHistory

---
**NOTE**
The upside to not implementing models in FireREST is that  FireREST is able to provide api calls to all
resources quickly, but you will need to construct api payloads for create and update
operations manually
---

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

FireREST uses basic authentication to login on fmc. In case your authentication
token times out, the api client will automatically refresh the session and retry
a failed operation. If all 3 refresh tokens have been used `Client` will try to
re-authenticate again.

#### Basic Authentication

```python
client = Client(hostname='fmc.example.com', username='firerest', password='Cisco123')
```

### Helper

A variety of helper functions can be used to translate object names to their
respective UUID values. Some resources may provide a `nameOrValue` or `name`
filter to find a resource based on their `value` or `name`, but in case you are
working with a resource that does not allow filtering you will need to use
helpers.

Since fmc rest api uses uuid values this is neccessary to find pre-existing objects by the name defined in fmc.

#### Get network object uuid by name

```python
name = 'NET_OBJ'
uuid = client.get_object_id('network', name)
```

#### Get accesspolicy uuid by name

```python
accesspolicy = 'ACCESSPOLICY'
accesspolicy_id = client.get_accesspolicy_id(name)
```

#### Get accesspolicy rule uuid by name

```python
accesspolicy = 'DEV-ACCESS-CONTROL-POLICY'
accessrule = 'PERMIT-INTERNET-ACCESS'

accesspolicy_id = client.get_accesspolicy_id(accesspolicy)
accessrule_id = client.get_accesspolicy_rule_id(accesspolicy_id, accessrule)
```

### Objects

#### Create network object

```python
net_obj = {
    'name': 'NetObjViaAPI',
    'value': '198.18.1.0/24',
}

response = client.create_objects('network', net_obj)
```

#### Get network object

```python
obj_name = 'NetObjViaAPI'
obj_id = client.get_object_id('network', obj_name)
obj = client.get_objects('network', obj_id)
```

#### Update network object

```python
obj_name = 'NetObjViaAPI'
obj_id = client.get_object_id('network', 'NetObjViaAPI')

net_obj = {
    'id': obj_id,
    'name': 'NetObjViaAPI',
    'value': '198.18.2.0/24',
}

response = client.update_object('network', obj_id, net_obj)
```

#### Delete network object

```python
obj_name = 'NetObjViaAPI'
obj_id = client.get_object_id('network', 'NetObjViaAPI')
response = client.delete_object('network', obj_id)
```


## Authors

Oliver Kaiser (oliver.kaiser@outlook.com)

## License

GNU General Public License v3.0 or later.

See [LICENSE](LICENSE) for the full text.
