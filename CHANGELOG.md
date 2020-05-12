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
