# 1.0.11 [2022-03-DD]

* Added support for FMC 7.1.0 api calls
  * chassis.get(...)
  * chassis.networkmodule.update(...)
  * chassis.networkmodule.get(...)
  * chassis.interface.get(...)
  * chassis.interface.evaluate_operation(...)
  * chassis.operational.sync_network_module(...)
  * chassis.operational.breakout_interfaces(...)
  * chassis.operational.join_interfaces(...)
  * cluster.ftddevicecluster.operational.command(...)
  * cluster.ftddevicecluster.readiness_check(...)
  * device.devicerecord.routing.policybasedroute.create(...)
  * device.devicerecord.routing.policybasedroute.get(...)
  * device.devicerecord.routing.policybasedroute.update(...)
  * device.devicerecord.routing.policybasedroute.delete(...)
  * health.tunnelstatus.get(...)
  * health.tunnelsummary.get(...)
  * netmap.host.create(...)
  * netmap.host.get(...)
  * netmap.host.delete(...)
  * netmap.vulnerability.create(...)
  * netmap.vulnerability.get(...)
  * netmap.vulnerability.delete(...)
  * object.aspathlist.create(...)
  * object.aspathlist.update(...)
  * object.aspathlist.delete(...)
  * object.expandedcommunitylist.create(...)
  * object.expandedcommunitylist.update(...)
  * object.expandedcommunitylist.delete(...)
  * object.standardcommunitylist.create(...)
  * object.standardcommunitylist.create(...)
  * object.standardcommunitylist.create(...)
  * object.standardaccesslist.create(...)
  * object.standardaccesslist.update(...)
  * object.standardaccesslist.delete(...)
  * object.extendedaccesslist.create(...)
  * object.extendedaccesslist.update(...)
  * object.extendedaccesslist.delete(...)
  * object.ipv4prefixlist.create(...)
  * object.ipv4prefixlist.update(...)
  * object.ipv4prefixlist.delete(...)
  * object.ipv6prefixlist.create(...)
  * object.ipv6prefixlist.update(...)
  * object.ipv6prefixlist.delete(...)
  * object.policylist.create(...)
  * object.policylist.update(...)
  * object.policylist.delete(...)
  * object.routemap.create(...)
  * object.routemap.update(...)
  * object.routemap.delete(...)
  * troubleshoot.packettracer.file.create(...)
  * troubleshoot.packettracer.file.get(...)
  * troubleshoot.packettracer.file.delete(...)
  * troubleshoot.packettracer.file.details.get(...)
  * troubleshoot.packettracer.trace(...)
  * troubleshoot.packettracer.pcaptrace(...) 
  * update.revert(...)
  * user.duoconfig.get(...)
  * user.duoconfig.update(...)

* Added support for missing older api calls
  * cluster.ftddevicecluster.create(...)
  * cluster.ftddevicecluster.update(...)
  * cluster.ftddevicecluster.delete(...)

# 1.0.10 [2022-02-19]

## Fixed

* incorrect api endpoint for object.dynamicobject (#57, #64). thanks @dheule for providing a fix
* missing refs in devicerecord for physicalinterface (#61)
* incorrect api endpoint for object.continent (#60)
* uuid check issues with object.applicationcategory (#59)
* removed incorrect delete calls for device.devicerecord.redundantinterface
* removed incorrect delete calls for device.devicerecord.subinterface
* removed incorrect delete calls for device.devicerecord.virtualswitch
* removed incorrect delete calls for device.devicerecord.virtualtunnelinterface
* removed incorrect delete calls for device.devicerecord.vlaninterface

# 1.0.9 [2021-10-19]

## Fixed

* requests were not retried when authentication token was refreshed (#53)
* `accesspolicy.category` exposed incorrect param before_category (#54)
* various devicerecord update calls incorrectly overrode the update function causing update calls to fail

# 1.0.8 [2021-08-03]

## Fixed

* boolean filter values were not parsed correctly resulted in incorrect filters being passed to FMC API
* added missing filter operations to `policy.accesspolicy.operational.hitcounts` `get` operation

# 1.0.7 [2021-07-25]

## New

* Added support for FMC 7.0.0 api calls
  * GET integration.fmchastatus
  * GET integration.securexconfig
  * GET object.anyconnectcustomattribute
  * GET object.anyconnectpackage
  * GET object.anyconnectprofile
  * CREATE, UPDATE, DELETE object.applicationfilter
  * GET object.certificatemap
  * CREATE, UPDATE, DELETE object.dnsservergroup
  * CREATE, GET, UPDATE, DELETE object.dynamicobject
  * CREATE, UPDATE, DELETE object.geolocation
  * GET object.grouppolicy
  * GET object.hostscanpackage
  * CREATE, GET, UPDATE, DELETE object.intrusionrule
  * CREATE, GET, UPDATE, DELETE object.intrusionrulegroup
  * GET object.ipv4addresspool
  * GET object.ipv6addresspool
  * CREATE, GET, UPDATE, DELETE object.localrealmuser
  * GET object.radiusservergroup
  * CREATE, GET, UPDATE, DELETE object.realm
  * GET object.sidnsfeed
  * GET object.sidnslist
  * GET object.sinetworkfeed
  * GET object.sinetworklist
  * GET object.sinkhole
  * GET object.ssoserver
  * GET bject.usage
  * GET policy.accesspolicy.securityintelligencepolicy
  * GET policy.dnspolicy
  * GET policy.dnspolicy.allowdnsrule
  * GET policy.dnspolicy.blockdnsrule
  * GET policy.dynamicaccesspolicy
  * GET policy.identitypolicy
  * CREATE, UPDATE, DELETE policy.intrusionpolicy
  * GET, UPDATE policy.intrusionpolicy.intrusionrulegroup
  * GET, UPDATE policy.intrusionpolicy.intrusionrule
  * CREATE, GET, UPDATE, DELETE policy.networkanalysispolicy
  * GET, UPDATE, DELETE policy.networkanalysispolicy.inspectorconfig
  * GET, UPDATE, DELETE policy.networkanalysispolicy.inspectoroverrideconfig
  * GET policy.ravpn
  * GET policy.ravpn.addressassignmensettings
  * GET policy.ravpn.certificatemapsettings
  * GET policy.ravpn.connectionprofile

## Fixed

* Authentication refresh failed due to incorrect object reference in utils.py

# 1.0.6 [2021-04-01]

## Fixed

* Bulk create/update failed due to bulk param not being set automatically for some resources
* RateLimiter error was not handled correctly leading to retry operations not being tried

# 1.0.5 [2021-03-19]

## Fixed

* `ChildResource` missing uuid by name lookup functionality (#45)
* Custom params causing container lookup by name to fail (#45)
* `job.taskstatuses` accessibility from `fmc` object (#47)
* Incorrect Namespace references in `update`, `upgradepackage` and `deployabledevices` Resources (#46)

## Fixed

# 1.0.4

## Fixed

* Fixed issue with container name resolution that caused incorrect params to be passed to GET_BY_ID operations
* Fixed an issue where HTTPErrors where incorrectly raised, causing confusing exceptions

# 1.0.3

## Changed

* Added dry_mode switch to FMC object. When using dry_mode PUT, POST and DELETE
* Operations are not executed and only logged to FireREST logger

## Fixed

* Added missing `Override` reference to host object

# 1.0.2

## New

* Added `Override` resource to all objects that support object overrides

# 1.0.1

## Fixed

* Fixed an issue where simplejson installation cause FireREST to be unusable
  due to requests library using simplejson instead of built-in json library
  causing simplejson exception to be thrown instead of json.DecodeError exception

# 1.0.0

1.0.0 is a major overhaul of the existing FireREST codebase. I decided to
refactor the whole project to provide a more structured way to interact with
FMC. Before 1.0.0 all calls to FMC were provided by a `Client` object which was
replaced by `FMC` that provides a hierarchical access to all resources on FMC.

## Changed

* Replaced `Client` object with `FMC`
* Provide structured access to api objects. e.g. `fmc.policy.accesspolicy.get`
* Provide more granular error handling using custom exceptions

# 0.1.8

## New

* Filtering options to all supported api calls

## Fixed

* Various s2svpn related operations that missed string interpolation

# 0.1.7

## New

* Health alert api calls for 6.7.0
* Additional id_by_name operations
* Better logging for requests

## Fixed

* Reauth was not triggered correctly when authentication failed


# 0.1.6

## New

* ResourceNotFound exception for 404 errors
* Additional api calls
  * S2svpn
  * vlaninterfaces
  * interfaceevents
  * devicecopyrequests
  * virtualrouter
  * inlinesets
  * prefilterpolicy
  * prefilterpolicy rules
  * accesspolicy defaultaction
  * device metrics
  * device commands

## Fixed

* Issue with incorrect default id values


# 0.1.5

## Changed

* Added additional unit tests for id_by_name operations
* Merged and enhanced hitcount implementation by @arnydo (#29)

## Fixed

* Issue with id_by_name helper functions caused by incorrect cache impl (#28)
* Nissing interface_id param for interface PUT operations (#30)

# 0.1.4

## Changed

* Added various tests for better qa

## Fixed

* Correctly sanitize payloads for put operations
* Corrected cache_result condition that did not match correctly


# 0.1.3

## Fixed

* Missing conversion from dict to json in _request helper

# 0.1.2

## Fixed

* Api call for getting audit records (#24)
* Incorrect base api calls by removing positional args (#23)

# 0.1.1

## Changed

* Dependency version pinning to minimum required software versions

# 0.1.0

## Fixed

* KeyError that occured when get request was launched that yielded an empty result (no items)
* Incorrect function call that caused getter for obj overrides to fail

# 0.0.9

## Changed

* Added version pinning for all dependencies
* Added tox integration for testing new releases
* Added cache option for costly getbyid operations using cache flag
* Added sessions so tcp connections are being reused for subsequent api calls
* Added better error handling and better retrying for rate limiting exception
* Added prefilterpolicy related crud operations
* Added minimum version requirements to api calls
* Rewrote tests with pytest instead of unittest
* Restructured project and moved default, exceptions and utils into their own files
* Renamed accesscontrolpolicy related crud operations

## Fixed

* #19

# 0.0.4

## New

* Changelog for new software releases
* Api calls for hapair monitoredinterfaces (read, update)
* Helper function to get primary device id from hapair
* Expandable option for get_depoyable_deployable_devices

## Changed

* Default paging change from 25 to 100

## Fixed

* Getbyid operations fails due to incorrect limit param
* Api calls for ftd ipv4/ipv6 static routing fails due to incorrect URLs
* Update ftd sub interface fails due to missing param
