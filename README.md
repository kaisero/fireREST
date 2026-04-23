[![python3](https://img.shields.io/badge/python-3.9+-blue.svg)](https://github.com/kaisero/fireREST/) [![pypi](https://img.shields.io/pypi/v/fireREST)](https://pypi.org/project/fireREST/) [![license](https://img.shields.io/badge/license-GPL%20v3.0-brightgreen.svg)](https://github.com/kaisero/fireREST/blob/master/LICENSE) [![status](https://img.shields.io/badge/status-beta-blue.svg)](https://github.com/kaisero/fireREST/) [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/kaisero/fireREST)


# FireREST

FireREST is a python library to interface with Cisco Firepower Management Center REST API. The goal of FireREST is to provide a simple SDK to programmatically interact with FMC.


## Features

* Authentication and automatic session refresh / re-authentication
* Rate-limit detection and automatic backoff and retry behavior
* Automatic squashing of paginated api payloads
* Sanitization of api payloads for create and update operations (automatically remove unsupported elements like links, metadata from payload)
* Detailed logging of api requests and responses
* API specific error handling using various custom exceptions for typical errors (e.g. ResourceAlreadyExists, UnprocessAbleEntityError, ...)
* Support for resource lookup by name instead of uuid for all CRUD operations

## Requirements

* Python >= 3.9

## Quickstart

### Installation

```bash
> pip install fireREST
```

### Import api client

```python
from fireREST import FMC
```

### Authentication (self-hosted)

FireREST uses basic authentication. In case your authentication token times out, the api client will automatically refresh the session and retry
a failed operation. If all 3 refresh tokens have been used up the connection object will try to re-authenticate again automatically.

```python
fmc = FMC(hostname='fmc.example.com', username='firerest', password='Cisco123', domain='Global')
```

> **_NOTE:_**  By default domain is set to `Global`

### Authentication (cdFMC/CDO)

fireREST uses Bearer token to authenticate. This token can be obtained from CDO cloud portal.

```python
fmc = FMC(hostname='example.app.eu.cdo.cisco.com', password='<CDO Token>', cdo=True)
```

### CRUD Operations

#### Objects

##### Create network object

```python
net_obj = {
    'name': 'NetObjViaAPI',
    'value': '198.18.1.0/24',
}

response = fmc.object.network.create(data=net_obj)
```

> **_NOTE:_**  in case a resource supports the `bulk` option `FireREST` will automatically perform a bulk operation if the `data` provided is of type `list`

##### Get all network objects

```python
net_objects = fmc.object.network.get()
```

##### Get specific network object

```python
net_objects = fmc.object.network.get(name='NetObjViaAPI')
```

> **_NOTE:_** You can access a resource either by `name` or `uuid`. If the resource supports a filtering by name FireREST will utilize the filter option, in case
> a Resource does not support filter params it will iterate through all resources to find a match

##### Update network object

```python
net_obj = fmc.object.network.get(name='NetObjViaAPI')
net_obj['name'] = 'RenamedNetObjViaAPI'
response = fmc.object.network.update(data=net_obj)
```

> **_NOTE:_**  FireREST automatically extracts the `id` field of the provided data `dict` to update the correct resource.

##### Delete network object

```python
response = fmc.object.network.delete(name='NetObjViaAPI')
```

## Supported operations

Since FireREST does not try to provide a python object model nearly all api calls up to version 7.4.0 are available which includes but is not limited to
the following CRUD operations:

```
├── assignment
│   └── policyassignment
├── audit
│   └── auditrecord
├── chassis
│   ├── interface
│   ├── networkmodule
│   └── operational
├── deployment
│   ├── deployabledevice
│   │   ├── deployment
│   │   └── pendingchanges
│   ├── deploymentrequest
│   ├── jobhistory
│   └── rollbackrequest
├── device
│   └── devicerecord
│       ├── bridgegroupinterface
│       ├── etherchannelinterface
│       ├── fpinterfacestatistics
│       ├── fplogicalinterface
│       ├── fpphysicalinterface
│       ├── inlineset
│       ├── interfaceevent
│       ├── operational
│       │   ├── command
│       │   └── metric
│       ├── physicalinterface
│       ├── redundantinterface
│       ├── routing
│       │   ├── bgp
│       │   ├── bgpgeneralsettings
│       │   ├── ipv4staticroute
│       │   ├── ipv6staticroute
│       │   ├── ospfinterface
│       │   ├── ospfv2route
│       │   ├── ospfv3interface
│       │   ├── policybasedroute
│       │   ├── staticroute
│       │   └── virtualrouter
│       │       ├── bgp
│       │       ├── ipv4staticroute
│       │       ├── ipv6staticroute
│       │       ├── ospfinterface
│       │       ├── ospfv2route
│       │       └── policybasedroute
│       ├── subinterface
│       ├── virtualswitch
│       ├── virtualtunnelinterface
│       └── vlaninterface
├── devicecluster
│   └── ftddevicecluster
│       └── operational
├── devicegroup
│   └── devicegrouprecord
├── devicehapair
│   └── ftddevicehapair
│       ├── failoverinterfacemacaddressconfig
│       └── monitoredinterface
├── health
│   ├── alert
│   ├── metric
│   ├── tunnelstatus
│   └── tunnelsummary
├── integration
│   ├── cloudeventsconfig
│   ├── cloudregion
│   ├── externallookup
│   ├── externalstorage
│   ├── fmchastatus
│   └── securexconfig
├── intelligence
│   ├── taxiiconfig
│   │   ├── collection
│   │   └── discoveryinfo
│   └── tid
│       ├── element
│       ├── incident
│       ├── indicator
│       ├── observable
│       ├── setting
│       └── source
├── job
│   └── taskstatus
├── netmap
│   ├── host
│   └── vulnerability
├── object
│   ├── anyconnectcustomattribute
│   │   └── override
│   ├── anyconnectpackage
│   ├── anyconnectprofile
│   ├── anyprotocolportobject
│   ├── application
│   ├── applicationcategory
│   ├── applicationfilter
│   ├── applicationproductivities
│   ├── applicationrisk
│   ├── applicationtag
│   ├── applicationtype
│   ├── aspathlist
│   ├── certenrollment
│   ├── certificatemap
│   ├── communitylist
│   ├── continent
│   ├── country
│   ├── dnsservergroup
│   │   └── override
│   ├── dynamicobject
│   │   └── mapping
│   ├── endpointdevicetype
│   ├── expandedcommunitylist
│   ├── extendedaccesslist
│   ├── fqdn
│   │   └── override
│   ├── geolocation
│   ├── globaltimezone
│   ├── grouppolicy
│   ├── host
│   │   └── override
│   ├── hostscanpackage
│   ├── icmpv4object
│   │   └── override
│   ├── icmpv6object
│   │   └── override
│   ├── ikev1ipsecproposal
│   ├── ikev1policy
│   ├── ikev2ipsecproposal
│   ├── ikev2policy
│   ├── interface
│   ├── interfacegroup
│   ├── intrusionrule
│   ├── intrusionrulegroup
│   ├── ipv4addresspool
│   │   └── override
│   ├── ipv4prefixlist
│   ├── ipv6addresspool
│   │   └── override
│   ├── ipv6prefixlist
│   ├── isesecuritygrouptag
│   ├── keychain
│   │   └── override
│   ├── network
│   │   └── override
│   ├── networkaddress
│   ├── networkgroup
│   │   └── override
│   ├── operational
│   │   └── usage
│   ├── policylist
│   ├── port
│   ├── portobjectgroup
│   │   └── override
│   ├── protocolportobject
│   │   └── override
│   ├── radiusservergroup
│   ├── range
│   │   └── override
│   ├── realm
│   ├── realmuser
│   ├── realmusergroup
│   ├── routemap
│   ├── securitygrouptag
│   ├── securityzone
│   ├── sidnsfeed
│   ├── sidnslist
│   ├── sinetworkfeed
│   ├── sinetworklist
│   ├── sinkhole
│   ├── siurlfeed
│   ├── siurllist
│   ├── slamonitor
│   ├── ssoserver
│   │   └── override
│   ├── standardaccesslist
│   ├── standardcommunitylist
│   ├── timerange
│   ├── timezone
│   │   └── override
│   ├── tunneltag
│   ├── url
│   │   └── override
│   ├── urlcategory
│   ├── urlgroup
│   │   └── override
│   ├── variableset
│   ├── vlangrouptag
│   │   └── override
│   └── vlantag
│       └── override
├── policy
│   ├── accesspolicy
│   │   ├── accessrule
│   │   ├── category
│   │   ├── defaultaction
│   │   ├── inheritancesettings
│   │   ├── loggingsettings
│   │   ├── operational
│   │   │   └── hitcounts
│   │   └── securityintelligencepolicy
│   ├── dnspolicy
│   │   ├── allowdnsrule
│   │   └── blockdnsrule
│   ├── dynamicaccesspolicy
│   ├── filepolicy
│   ├── ftdnatpolicy
│   │   ├── autonatrule
│   │   ├── manualnatrule
│   │   └── natrule
│   ├── ftds2svpn
│   │   ├── advancedsettings
│   │   ├── endpoint
│   │   ├── ikesettings
│   │   └── ipsecsettings
│   ├── identitypolicy
│   ├── intrusionpolicy
│   │   ├── intrusionrule
│   │   └── intrusionrulegroup
│   ├── networkanalysispolicy
│   │   ├── inspectorconfig
│   │   └── inspectoroverrideconfig
│   ├── prefilterpolicy
│   │   ├── defaultaction
│   │   ├── operational
│   │   │   └── hitcounts
│   │   └── prefilterrule
│   ├── ravpn
│   │   ├── addressassignmentsettings
│   │   ├── certificatemapsettings
│   │   └── connectionprofile
│   ├── snmpalert
│   └── syslogalert
├── system
│   └── info
│       ├── domain
│       └── serverversion
├── troubleshoot
│   └── packettracer
│       └── file
├── update
│   └── upgradepackage
│       └── applicabledevice
└── user
    ├── authrole
    ├── duoconfig
    └── ssoconfig
```

## Troubleshooting

### UnprocessableEntityError

You might see an `UnprocessableEntityError` exception when you try to execute  `CREATE`or `UPDATE` operations. Depending on the API endpoint the error message from FMC might not contain enough information to pinpoint what is causing the issue. In this case I would recommend using `pigtail` on FMC to get more detailed information.

#### Example

In this example we are trying to create an object override, but the field `value` is invalid. The subnet mask chosen is not correct, which will cause the FMC API to respond with an UnprocessAbleEntity error.

````bash
data = {
    "overrides": {
        "parent": {
            "id": "00505699-76B7-0ed3-0000-077309525737"
        },
        "target": {
            "id": "0ff8161e-096e-11eb-8ec0-cb721f246e60",
            "type": "Device"
        }
    },
    "value": "198.18.201.0/241",
    "name": "NetObjWithOverrides",
    "id": "00505699-76B7-0ed3-0000-077309525737"
}
fmc.object.network.update(data=data)
````

On FMC we can use the `pigtail` utility to tail the logfile on the Tomcat webserver hosting the REST API. Using this method we can monitor the APIs response and get some additional information on the error

````bash
> expert
admin@fmc:/Volume/home/admin# sudo su -
root@fmc:/Volume/home/admin# pigtail TCAT
````

Here we see that a Java exception has been thrown, indicating that the request failed due an invalid ip address being passed

```
TCAT: 02-02 15:36:33 INFO: 172.21.100.145	-	-	443	PUT	/api/fmc_config/v1/domain/b76ff587-9224-65c7-d2af-000000000000/object/networks/00505699-76B7-0ed3-0000-077309525737	-	400	-	301	169	https://fmc.example.com	FireREST/1.0.0	-
TCAT: 02-02 15:34:33 [ajp-nio-127.0.0.1-9009-exec-1] ERROR com.cisco.api.external.rest.common.resource.ContainerServerResource - **Invalid IP Address**
TCAT: 02-02 15:34:33 APIException:Invalid IP Address
```

## Authors

Oliver Kaiser (oliver.kaiser@outlook.com)

## Maintainers

Rafal Chrabaszcz (rchrabas@cisco.com)

## License

GNU General Public License v3.0 or later.

See [LICENSE](LICENSE) for the full text.
