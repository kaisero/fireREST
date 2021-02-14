.. toctree::
   :maxdepth: 3

FireREST Documentation
======================

FireREST is a python library to interface with Cisco Firepower Management Center REST API.
The goal of FireREST is to provide a simple SDK to programmatically interact with FMC.


**Features**

* Authentication and automatic session refresh / re-authentication
* Rate-limit detection and automatic backoff and retry behavior
* Automatic squashing of paginated api payloads
* Sanitization of api payloads for create and update operations (automatically remove unsupported elements like links, metadata from payload)
* Detailed logging of api requests and responses
* API specific error handling using various custom exceptions for typical errors (e.g. ResourceAlreadyExists, UnprocessAbleEntityError, ...)
* Support for resource lookup by name instead of uuid for all CRUD operations

Requirements
======================

* Python >= 3.7

Installation
============

.. code-block:: shell

  pip install fireREST

Quickstart
==========

Import api client

.. code-block:: python

  from fireREST import FMC

FireREST uses basic authentication. In case your authentication token times out, the api client will automatically refresh the session and retry
a failed operation. If all 3 refresh tokens have been used up the connection object will try to re-authenticate again automatically.

.. code-block:: python

   fmc = FMC(hostname='fmc.example.com', username='firerest', password='Cisco123', domain='Global')

.. note::

   By default domain is set to `Global`

===============
CRUD Operations
===============

Objects
-------

Create network object

.. code-block:: python

   net_obj = {
       'name': 'NetObjViaAPI',
       'value': '198.18.1.0/24',
   }

response = fmc.object.network.create(data=net_obj)


.. note::

   in case a resource supports the `bulk` option `FireREST` will automatically perform a bulk operation if the `data` provided is of type `list`

Get all network objects

.. code-block::python

  net_objects = fmc.object.network.get()


Get specific network object

.. code-block:: python

  net_objects = fmc.object.network.get(name='NetObjViaAPI')

.. note::

   You can access a resource either by `name` or `uuid`. If the resource supports a filtering by name FireREST will utilize the filter option, in case
   a Resource does not support filter params it will iterate through all resources to find a match

Update network object

.. code-block:: python

   net_obj = fmc.object.network.get(name='NetObjViaAPI')
   net_obj['name'] = 'RenamedNetObjViaAPI'
   response = fmc.object.network.update(data=net_obj)


.. note::

   FireREST automatically extracts the `id` field of the provided data `dict` to update the correct resource.

Delete network object

.. code-block:: python

  response = fmc.object.network.delete(name='NetObjViaAPI')


Supported operations
====================

Since FireREST does not try to provide a python object model nearly all api calls up to version 6.7.0 are available which includes but is not limited to
the following CRUD operations:

.. code-block::

   ├── assignment
   │   └── policyassignment
   ├── audit
   │   └── auditrecord
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
   │       │   ├── staticroute
   │       │   └── virtualrouter
   │       ├── subinterface
   │       ├── virtualswitch
   │       ├── virtualtunnelinterface
   │       └── vlaninterface
   ├── devicecluster
   │   └── ftddevicecluster
   ├── devicegroup
   │   └── devicegrouprecord
   ├── devicehapair
   │   └── ftddevicehapair
   │       ├── failoverinterfacemacaddressconfig
   │       └── monitoredinterface
   ├── health
   │   ├── alert
   │   └── metric
   ├── integration
   │   ├── cloudeventsconfig
   │   ├── cloudregion
   │   ├── externallookup
   │   └── externalstorage
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
   ├── object
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
   │   ├── communitylist
   │   ├── continent
   │   ├── country
   │   ├── dnsservergroup
   │   ├── endpointdevicetype
   │   ├── expandedcommunitylist
   │   ├── extendedaccesslist
   │   ├── fqdn
   │   │   └── override
   │   ├── geolocation
   │   ├── globaltimezone
   │   ├── host
   │   │   └── override
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
   │   ├── ipv4prefixlist
   │   ├── ipv6prefixlist
   │   ├── isesecuritygrouptag
   │   ├── keychain
   │   │   └── override
   │   ├── network
   │   │   └── override
   │   ├── networkaddress
   │   ├── networkgroup
   │   │   └── override
   │   ├── policylist
   │   ├── port
   │   ├── portobjectgroup
   │   │   └── override
   │   ├── protocolportobject
   │   │   └── override
   │   ├── range
   │   │   └── override
   │   ├── realmuser
   │   ├── realmusergroup
   │   ├── routemap
   │   ├── securitygrouptag
   │   ├── securityzone
   │   ├── siurlfeed
   │   ├── siurllist
   │   ├── slamonitor
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
   │   │   └── operational
   │   │       └── hitcounts
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
   │   ├── intrusionpolicy
   │   │   └── intrusionrule
   │   ├── prefilterpolicy
   │   │   ├── defaultaction
   │   │   ├── operational
   │   │   │   └── hitcounts
   │   │   └── prefilterrule
   │   ├── snmpalert
   │   └── syslogalert
   ├── system
   │   └── info
   │       ├── domain
   │       └── serverversion
   ├── update
   │   └── upgradepackage
   │       └── applicabledevice
   └── user
       ├── authrole
       └── ssoconfig



Modules
=======

:ref:`modindex`
