# 1.0.2

## Enhancements

Added `Override` resource to all objects that support object overrides

# 1.0.1

## Bugfixes

Fixed an issue where simplejson installation cause FireREST to be unusable
due to requests library using simplejson instead of built-in json library
causing simplejson exception to be thrown instead of json.DecodeError exception

# 1.0.0

1.0.0 is a major overhaul of the existing FireREST codebase. I decided to
refactor the whole project to provide a more structured way to interact with
FMC. Before 1.0.0 all calls to FMC were provided by a `Client` object which was
replaced by `FMC` that provides a hierarchical access to all resources on FMC.

## Enhancements

Replaced `Client` object with `FMC`
Provide structured access to api objects. e.g. `fmc.policy.accesspolicy.get`
Provide more granular error handling using custom exceptions

# 0.1.8

## Bugfixes

Fixed various s2svpn related operations that missed string interpolation

## Enhancements

Added filtering options to all supported api calls

# 0.1.7

## Bugfixes

Fixed issue where reauth was not triggered correctly

## Enhancements

Added health alert api calls for 6.7.0
Added additional id_by_name operations
Added better logging for requests

# 0.1.6

## Bugfixes

Fixed issue with incorrect default id values

## Enhancements

Added ResourceNotFound exception for 404 errors

Added additional api calls
* s2svpn
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

Added vrf support for applicable device api calls

Renamed get_id functions (removed _by_name suffix)

# 0.1.5

## Bugfixes

Fixed issue with id_by_name helper functions caused by incorrect cache impl (#28)
Fixed missing interface_id param for interface PUT operations (#30)

## Enhancements

Added additional unit tests for id_by_name operations
Merged and enhanced hitcount implementation by @arnydo (#29)

# 0.1.4

## Bugfixes

Added a fix to correctly sanitize payloads for put operations
Corrected cache_result condition that did not match correctly

## Enhancements

Added various tests for better qa

# 0.1.3

## Bugfixes

Fixed missing conversion from dict to json in _request helper

# 0.1.2

## Bugfixes

Corrected api call for getting audit records (#24)
Corrected incorrect base api calls by removing positional args (#23)

# 0.1.1

## Enhancements

Changed dependency version pinning to minimum required software versions

# 0.1.0

## Bugfixes

Fixed a KeyError that occured when get request was launched that yielded an empty result (no items)
Fixed a incorrect function call that caused getter for obj overrides to fail

# 0.0.9

## Bugfixes

Fixed issue mentioned in (#19)

## Enhancements

Added version pinning for all dependencies
Added tox integration for testing new releases
Added cache option for costly getbyid operations using cache flag
Added sessions so tcp connections are being reused for subsequent api calls
Added better error handling and better retrying for rate limiting exception
Added prefilterpolicy related crud operations
Added minimum version requirements to api calls
Rewrote tests with pytest instead of unittest
Restructured project and moved default, exceptions and utils into their own files
Renamed accesscontrolpolicy related crud operations

# 0.0.4

## Bugfixes

* getbyid operations fails due to incorrect limit param
* api calls for ftd ipv4/ipv6 static routing fails due to incorrect URLs
* update ftd sub interface fails due to missing param

## Enhancements

* Add api calls for hapair monitoredinterfaces (read, update)
* Add helper function to get primary device id from hapair
* Add expandable option for get_depoyable_deployable_devices
* Default paging change from 25 to 100
