[![python3](https://img.shields.io/badge/python-3.7+-blue.svg)](https://github.com/kaisero/fireREST/) [![pypi](https://img.shields.io/pypi/v/fireREST)](https://pypi.org/project/fireREST/) [![license](https://img.shields.io/badge/license-GPL%20v3.0-brightgreen.svg)](https://github.com/kaisero/fireREST/blob/master/LICENSE) [![status](https://img.shields.io/badge/status-alpha-blue.svg)](https://github.com/kaisero/fireREST/) [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/kaisero/fireREST)


# FireREST

FireREST is a python library to interface with Cisco Firepower Management Center REST API.

## Features

* Authentication and automatic session refresh / re-authentication
* Rate-limit detection and automatic backoff and retry behavior
* Automatic squashing of paginated api payloads
* Sanitization of api payloads for create and update operations
* Detailed logging of api calls
* API specific error handling using various custom exceptions
* Support for resource lookup by name instead of uuid for all CRUD operations

## Requirements

* Python >= 3.7

## Quickstart

### Installation

```bash
pip install fireREST
```

### Import api client

```python
from fireREST import FMC
```

### Authentication

FireREST uses basic authentication. In case your authentication
token times out, the api client will automatically refresh the session and retry
a failed operation. In case all 3 refresh tokens have been the connection object will try to
re-authenticate again automatically.

```python
fmc = FMC(hostname='fmc.example.com', username='firerest', password='Cisco123', domain='Global')
```

> **_NOTE:_**  By default `Global` is used as domain

### Objects

#### Create network object

```python
net_obj = {
    'name': 'NetObjViaAPI',
    'value': '198.18.1.0/24',
}

response = fmc.object.network.create(data=net_obj)
```

> **_NOTE:_**  In case a resource supports the `bulk` option `FireREST` will automatically append `bulk=True` to
> params if the `data` provided is of type `list` and not `dict`

#### Get all network objects

```python
net_objects = fmc.object.network.get()
```

#### Get specific network object

```python
net_objects = fmc.object.network.get(name='NetObjViaAPI')
```

> **_NOTE:_** You can access resource either by `name` or `uuid`. If a name is specified FireREST will use
> a filter if supported by the api resource of iterate through all existing resources to find a match

#### Update network object

```python
net_obj = fmc.object.network.get(name='NetObjViaAPI')
net_obj['name'] = 'RenamedNetObjViaAPI'
response = fmc.object.network.update(data=net_obj)
```

> **_NOTE:_**  FireREST automatically extracts the `id` field of the provided data `dict` to update the correct resource

#### Delete network object

```python
response = fmc.object.network.delete(name='NetObjViaAPI')
```

## Supported operations

Since FireREST does not try to provide a python object model nearly all api
calls up to version 6.7.0 are available which includes but is not limited to
the following CRUD operations:

```
├── assignment
│   ├── policyassignment
├── audit
│   ├── auditrecord
├── deployment
│   ├── deployabledevice
│   │   ├── deployment
│   │   ├── pendingchanges
│   ├── deploymentrequest
│   ├── jobhistory
│   └── rollbackrequest
├── device
│   ├── devicerecord
│   │   ├── bridgegroupinterface
│   │   ├── etherchannelinterface
│   │   ├── fpinterfacestatistics
│   │   ├── fplogicalinterface
│   │   ├── fpphysicalinterface
│   │   ├── inlineset
│   │   ├── interfaceevent
│   │   ├── operational
│   │   │   ├── command
│   │   │   ├── metric
│   │   ├── physicalinterface
│   │   ├── redundantinterface
│   │   ├── routing
│   │   │   ├── bgp
│   │   │   ├── bgpgeneralsettings
│   │   │   ├── ipv4staticroute
│   │   │   ├── ipv6staticroute
│   │   │   ├── ospfinterface
│   │   │   ├── ospfv2route
│   │   │   ├── ospfv3interface
│   │   │   ├── staticroute
│   │   │   └── virtualrouter
│   │   ├── subinterface
│   │   ├── virtualswitch
│   │   ├── virtualtunnelinterface
│   │   └── vlaninterface
├── devicecluster
│   ├── ftddevicecluster
├── devicegroup
│   ├── devicegrouprecord
├── devicehapair
│   ├── ftddevicehapair
│   │   ├── failoverinterfacemacaddressconfig
│   │   ├── monitoredinterface
├── health
│   ├── alert
│   ├── metric
├── integration
│   ├── cloudeventsconfig
│   ├── cloudregion
│   ├── externallookup
│   ├── externalstorage
├── intelligence
│   ├── taxiiconfig
│   │   ├── collection
│   │   ├── discoveryinfo
│   └── tid
│       ├── element
│       ├── incident
│       ├── indicator
│       ├── observable
│       ├── setting
│       └── source
├── job
│   └── taskstatus
├── object
│   ├── anyprotocolportobject
│   ├── application
│   ├── applicationcategory
│   ├── applicationfilter
│   ├── applicationproductivities
│   ├── applicationrisk
│   ├── applicationtag
│   ├── applicationtype
│   ├── aspathlist
│   ├── certenrollment
│   ├── communitylist
│   ├── continent
│   ├── country
│   ├── dnsservergroup
│   ├── endpointdevicetype
│   ├── expandedcommunitylist
│   ├── extendedaccesslist
│   ├── fqdn
│   ├── geolocation
│   ├── globaltimezone
│   ├── host
│   ├── icmpv4object
│   ├── icmpv6object
│   ├── ikev1ipsecproposal
│   ├── ikev1policy
│   ├── ikev2ipsecproposal
│   ├── ikev2policy
│   ├── interface
│   ├── interfacegroup
│   ├── ipv4prefixlist
│   ├── ipv6prefixlist
│   ├── isesecuritygrouptag
│   ├── keychain
│   ├── network
│   ├── networkaddress
│   ├── networkgroup
│   ├── policylist
│   ├── port
│   ├── portobjectgroup
│   ├── protocolportobject
│   ├── range
│   ├── realmuser
│   ├── realmusergroup
│   ├── routemap
│   ├── securitygrouptag
│   ├── securityzone
│   ├── siurlfeed
│   ├── siurllist
│   ├── slamonitor
│   ├── standardaccesslist
│   ├── standardcommunitylist
│   ├── timerange
│   ├── timezone
│   ├── tunneltag
│   ├── url
│   ├── urlcategory
│   ├── urlgroup
│   ├── variableset
│   ├── vlangrouptag
│   └── vlantag
├── policy
│   ├── accesspolicy
│   │   ├── accessrule
│   │   ├── category
│   │   ├── defaultaction
│   │   ├── inheritancesettings
│   │   ├── loggingsettings
│   │   ├── operational
│   │   │   ├── hitcounts
│   ├── filepolicy
│   ├── ftdnatpolicy
│   │   ├── autonatrule
│   │   ├── manualnatrule
│   │   ├── natrule
│   ├── ftds2svpn
│   │   ├── advancedsettings
│   │   ├── endpoint
│   │   ├── ikesettings
│   │   ├── ipsecsettings
│   ├── intrusionpolicy
│   │   ├── intrusionrule
│   ├── prefilterpolicy
│   │   ├── defaultaction
│   │   ├── operational
│   │   │   ├── hitcounts
│   │   ├── prefilterrule
│   ├── snmpalert
│   └── syslogalert
├── system
│   ├── info
│   │   ├── domain
│   │   └── serverversion
├── update
│   └── upgradepackage
│       ├── applicabledevice
└── user
    ├── authrole
    └── ssoconfig
```

## Authors

Oliver Kaiser (oliver.kaiser@outlook.com)

## License

GNU General Public License v3.0 or later.

See [LICENSE](LICENSE) for the full text.
