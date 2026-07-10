# Unreleased

## Breaking Changes

* `policy.ftds2svpn.ipseccryptomap` moved to `policy.ravpn.ipseccryptomap`. The `ftds2svpns` container never had an `ipseccryptomaps` endpoint in any spec version; all calls were returning 404.
* `policy.ftds2svpn.s2svpnsummary` moved to `policy.s2svpnsummary`. The resource is a top-level list endpoint and was never a child of `FtdS2sVpn`.
* `intelligence.tid.*` and `intelligence.taxiiconfig.*` URL builder now includes the required `/domain/{domainUUID}` segment. All TID and TaxiiConfig calls were returning 404 previously.
* `integration.ebssnapshot` path corrected from `/integration/ebssnapshots/` to `/integration/ebssnapshot/` (singular).
* `policy.policylock` path corrected from `/policy/policylocks/` to `/policy/operational/policylocks`.
* `object.operational.usage` path corrected from `/objects/operational/usage` to `/object/operational/usage`.
* `health.csdac` removed. The `/health/csdac` endpoint was removed from the FMC API in 7.4.x.

## New

* Added granular HTTP exception types to `fireREST.exceptions` based on the FMC ResponseStructure:
  * `BadRequestError` — HTTP 400 (invalid parameters, missing fields, invalidated policy object)
  * `MethodNotAllowedError` — HTTP 405 (method not permitted on this resource)
  * `ServerError` — HTTP 5xx catch-all for FMC server-side failures
  * `RateLimitError` — HTTP 429 rate limit exceeded (canonical rename of `RateLimitException`)
  * `ConcurrentRequestError` — HTTP 429 when more than 10 parallel connections from the same IP
  * `RateLimitWriteError` — HTTP 429 when a parallel write operation is blocked
  * `RateLimitException` preserved as a backward-compatible alias for `RateLimitError`

* Added `search` namespace with four discovery endpoints:
  * search.device.get(...)
  * search.glob.get(...)
  * search.object.get(...)
  * search.policy.get(...)
* Added `object.extendedcommunitylist` resource:
  * object.extendedcommunitylist.get(...)
  * object.extendedcommunitylist.create(...)
  * object.extendedcommunitylist.update(...)
  * object.extendedcommunitylist.delete(...)
  * object.extendedcommunitylist.override.get(...)
* Added `object.localrealmuser` resource:
  * object.localrealmuser.get(...)
  * object.localrealmuser.create(...)
  * object.localrealmuser.update(...)
  * object.localrealmuser.delete(...)
* Added VXLAN interface resources:
  * device.devicerecord.vniinterface.get(...)
  * device.devicerecord.vniinterface.create(...)
  * device.devicerecord.vniinterface.update(...)
  * device.devicerecord.vniinterface.delete(...)
  * device.devicerecord.vteppolicy.get(...)
  * device.devicerecord.vteppolicy.create(...)
  * device.devicerecord.vteppolicy.update(...)
  * device.devicerecord.vteppolicy.delete(...)
* Added ECMP zone and OSPFv3 route resources:
  * device.devicerecord.routing.ecmpzone.get(...)
  * device.devicerecord.routing.ecmpzone.create(...)
  * device.devicerecord.routing.ecmpzone.update(...)
  * device.devicerecord.routing.ecmpzone.delete(...)
  * device.devicerecord.routing.ospfv3route.get(...)
  * device.devicerecord.routing.virtualrouter.ecmpzone.get(...)
  * device.devicerecord.routing.virtualrouter.ecmpzone.create(...)
  * device.devicerecord.routing.virtualrouter.ecmpzone.update(...)
  * device.devicerecord.routing.virtualrouter.ecmpzone.delete(...)
* Added `policy.ravpn.ipseccryptomap` resource (moved from `policy.ftds2svpn.ipseccryptomap`):
  * policy.ravpn.ipseccryptomap.get(...)
  * policy.ravpn.ipseccryptomap.update(...)
* Added top-level `policy.s2svpnsummary` resource (moved from `policy.ftds2svpn.s2svpnsummary`):
  * policy.s2svpnsummary.get(...)
* Added FMC 7.6 support — new `templates` namespace with full device template management:
  * templates.devicetemplate.get/create/update/delete(...)
  * templates.devicetemplate.apply(data, container_uuid=...)
  * templates.devicetemplate.generate(data)
  * templates.devicetemplate.association.get/delete(...)
  * templates.devicetemplate.defaultmodelmapping.get(...)
  * templates.devicetemplate.modelmapping.get/create/update/delete(...)
  * templates.devicetemplate.objectoverride.get/update(...)
  * templates.devicetemplate.templateinterface.get/create/delete(...)
  * templates.devicetemplate.templatevariable.get(...)
  * templates.devicetemplate.vpnsetting.get/create/update/delete(...)
  * templates.supporteddevicemodel.get(...)
* Added FMC 7.6 `analysis.identifieduser` resource:
  * analysis.identifieduser.get(...)
  * analysis.identifieduser.delete(...)
* Added FMC 7.6 `chassis.switch_mode_readiness_check(data)` method
* Added FMC 7.6 device resources:
  * device.ltpdevicerecord.get/delete(...)
  * device.bulkregistration.create(...)
  * device.downloadsamplecsv.get(...)
* Added FMC 7.6 `health.event` resource:
  * health.event.get(...)
* Added FMC 7.6 object resources:
  * object.macaddresspool.get/create/update/delete(...)
  * object.macaddresspool.override.get(...)
  * object.samlrealmuserandgroup.get(...)
  * object.variable.get/create/update/delete(...)
  * object.downloadrealm.create(...)
  * object.operational.realmstatus.get(...)
  * object.operational.testrealm.create(...)
* Added FMC 7.6 write operations to `policy.healthpolicy`:
  * policy.healthpolicy.create/update/delete(...)
* Added FMC 7.6 troubleshoot profiler resources:
  * troubleshoot.cpuprofiler.module.get/create(...)
  * troubleshoot.snortprofiler.rule.get/create(...)
* Added FMC 7.7 write operations to OSPFv2/v3 routing resources:
  * device.devicerecord.routing.ospfv2route.create/update/delete(...)
  * device.devicerecord.routing.ospfv3interface.create/update/delete(...)
  * device.devicerecord.routing.ospfv3route.create/update/delete(...)
  * device.devicerecord.routing.virtualrouter.ospfv2route.create/update/delete(...)
  * device.devicerecord.routing.virtualrouter.ospfinterface.create/update/delete(...)
* Added FMC 7.7 device certificate resources:
  * device.certificate.get(...)
  * device.certificatesexportdata.get(...)
  * device.managecertificate.create(...)
  * device.devicerecord.operational.outofbandchange.get/create(...)
* Added FMC 7.7 `health.aggregatemetric` resource:
  * health.aggregatemetric.get(...)
* Added FMC 7.7 `integration.aiops` sub-namespace:
  * integration.aiops.aiconfiguration.get/create(...)
  * integration.aiops.tsdbupload.create(...)
  * integration.aiops.tsdbuploadstatus.get(...)
* Added FMC 7.7 `integration.cloudintegration` resource:
  * integration.cloudintegration.get(...)
* Added FMC 7.7 object resources:
  * object.certenrollment.override.get(...)
  * object.serviceaccessobject.get/create/update/delete(...)
  * object.serviceaccessobject.override.get(...)
* Added FMC 7.7 `policy.ftdplatformsettingspolicy` children:
  * policy.ftdplatformsettingspolicy.bannersetting.get/update(...)
  * policy.ftdplatformsettingspolicy.eventlist.get/create/update/delete(...)
  * policy.ftdplatformsettingspolicy.sshaccesssetting.get/create/update/delete(...)
* Added FMC 7.7 write operation to `policy.accesspolicy.securityintelligencepolicy`:
  * policy.accesspolicy.securityintelligencepolicy.update(...)
* Added FMC 7.7 `troubleshoot.radkit` sub-namespace:
  * troubleshoot.radkit.service.get/create(...)
* Added FMC 10.0 `analysis.filter` resource:
  * analysis.filter.get/create/update/delete(...)
* Added FMC 10.0 `device.bulkcommand` resource:
  * device.bulkcommand.create(...)
* Added FMC 10.0 `device.devicerecord.universalzerotrustsetting` resource:
  * device.devicerecord.universalzerotrustsetting.get/update(...)
* Added FMC 10.0 integration resources:
  * integration.ftdcloudstatus.get(...)
  * integration.metricconfiguration.get/create(...)
  * integration.splunkprofile.get/create/update/delete(...)
* Added FMC 10.0 `policy.accesspolicy` children:
  * policy.accesspolicy.advancedloggingsetting.get/update(...)
  * policy.accesspolicy.evesetting.get/update(...)
* Added FMC 10.0 `policy.universalzerotrustpolicy` resource:
  * policy.universalzerotrustpolicy.get/update(...)
  * policy.universalzerotrustpolicy.universalzerotrustrule.get/create/update/delete(...)
* Added FMC 10.0 write operations to `policy.dnspolicy`:
  * policy.dnspolicy.create/update/delete(...)
  * policy.dnspolicy.dnsrule.get/create/update/delete(...)
* Added FMC 10.0 write operations to `policy.identitypolicy`:
  * policy.identitypolicy.create/update/delete(...)
  * policy.identitypolicy.identitycategory.get/create/update/delete(...)
  * policy.identitypolicy.identityrule.get/create/update/delete(...)
* Added FMC 10.0 `policy.decryptionpolicy.standardmodeconfiguration` resource:
  * policy.decryptionpolicy.standardmodeconfiguration.get/update(...)
* Added FMC 10.0 `policy.ftdplatformsettingspolicy.externalauthsetting` resource:
  * policy.ftdplatformsettingspolicy.externalauthsetting.get/update(...)
* Added FMC 10.0 `updates` namespace:
  * updates.contentupdate.get/update(...)
  * updates.contentupdateoperation.create(...)
  * updates.deviceupgradeinfo.get(...)
* Added FMC 10.0 `user.externalauth` sub-namespace:
  * user.externalauth.externalauth.get/update(...)
  * user.externalauth.applyexternalauth.create(...)
  * user.externalauth.fetchldapattributes.create(...)
  * user.externalauth.fetchldapdns.create(...)
  * user.externalauth.authconfigobject.get(...)
  * user.externalauth.ldapconfigobject.get/create/update/delete(...)
  * user.externalauth.radiusconfigobject.get/create/update/delete(...)
* Added FMC 10.0 `troubleshoot.packettracer.pcapdetail` resource:
  * troubleshoot.packettracer.pcapdetail.get/create(...)

## Fixed

* Fixed HTTP 403 responses always raising `AuthorizationError` instead of falling through to `GenericApiError` when response text did not match the expected substring.
* Fixed HTTP 405 responses always raising `MethodNotAllowedError` instead of falling through to `GenericApiError` when response text did not match the expected substring.
* Fixed HTTP 5xx responses beyond 500 (502, 503, 504) falling through to `GenericApiError` instead of raising `ServerError`.
* Fixed HTTP 429 responses not distinguishing between rate limit, concurrent connection, and parallel write errors; now raises `RateLimitWriteError` or `ConcurrentRequestError` as appropriate.
* Fixed TID namespace URL builder missing `/domain/{domainUUID}` segment (all `intelligence.tid.*` calls returned 404).
* Fixed TaxiiConfig `collection` and `discoveryinfo` PATH including spurious `/{uuid}` suffix for POST-only endpoints.
* Fixed `AllowDnsRule` PATH using singular `allowdnsrule` instead of plural `allowdnsrules`, and incorrectly appending `/{uuid}` to a list-only endpoint.
* Fixed `BlockDnsRule` PATH using singular `blockdnsrule` instead of plural `blockdnsrules`, and incorrectly appending `/{uuid}` to a list-only endpoint.
* Fixed `EbsSnapshot` PATH using plural `ebssnapshots` instead of singular `ebssnapshot`.
* Fixed `PolicyLock` PATH missing `/operational/` segment and incorrectly appending `/{uuid}`.
* Fixed `Usage` PATH using `/objects/` instead of `/object/`.
* Fixed `Hitcount` (AccessPolicy and PrefilterPolicy) PATH appending `/{uuid}` to a filter-based list endpoint; implemented `update()` and `delete()` which were no-ops returning without making any HTTP call.
* Fixed `S2sVpnSummary` implemented as `ChildResource` of `FtdS2sVpn` with a non-existent container path; converted to top-level `Resource`.
* Fixed `PreviewChanges` PATH appending `/{uuid}` to a list-only endpoint.
* Fixed `ValidationResults` PATH appending `/{uuid}` to a list-only endpoint.
* Fixed `DownloadReport` (deployment) PATH appending `/{uuid}` to a list-only endpoint.
* Fixed `EmailReport` PATH appending `/{uuid}` and declaring `MINIMUM_VERSION_REQUIRED_GET` for a CREATE-only endpoint.
* Fixed `FpInterfaceStatistics` PATH appending `/{uuid}` to a list-only endpoint.
* Fixed `ManagementConvergenceMode` PATH appending `/{uuid}` to a list/create-only endpoint.
* Fixed `TestUmbrellaConnection` PATH missing `/operational/` segment.
* Fixed `JobHistory` `SUPPORTED_FILTERS` referencing `device_uuid` which does not exist in the `FILTERS` mapping; corrected to `device_uuids`.
* Fixed `NatRule` `section` misplaced in `SUPPORTED_FILTERS`; moved to `SUPPORTED_PARAMS` so it is sent as a query parameter instead of a filter value.
* Fixed `ChassisInterface` `operation` misplaced in `SUPPORTED_PARAMS`; moved to `SUPPORTED_FILTERS` so it is sent as `filter=operation:...`.
* Fixed missing `FILTERS` mapping entries for `entity_uuid`, `parent_entity_types`, `parent_uuid`, `query_function`, `regex_filter`, `source`, `step`, and `uuid`; absence caused `KeyError` at runtime when these filter kwargs were passed.

# 1.3.0 [2026-06-12]

## Breaking Changes

* `policy.prefilterpolicy.accessrule` renamed to `prefilterrule`.
* `device.devicerecord.operational.command.get()` filter is now correctly passed as a list to `utils.search_filter()`.

## New

* Added support for FMC 7.4.0 api calls
  * analysis.activesessions.get(...)
  * analysis.activesessions.delete(...)
  * analysis.useractivity.get(...)
  * analysis.useractivity.delete(...)
  * audit.configchanges.get(...)
  * changemanagement.ticket.create(...)
  * changemanagement.ticket.get(...)
  * changemanagement.ticket.update(...)
  * changemanagement.ticket.previewchanges.get(...)
  * changemanagement.ticket.validationresults.get(...)
  * chassis.appinfo.get(...)
  * chassis.chassisetherchannelinterface.create(...)
  * chassis.chassisetherchannelinterface.get(...)
  * chassis.chassisetherchannelinterface.update(...)
  * chassis.chassisetherchannelinterface.delete(...)
  * chassis.chassisinterface.get(...)
  * chassis.chassisinterfaceevent.create(...)
  * chassis.chassisinterfaceevent.get(...)
  * chassis.chassissnmpsettings.get(...)
  * chassis.chassissnmpsettings.update(...)
  * chassis.chassissubinterface.create(...)
  * chassis.chassissubinterface.get(...)
  * chassis.chassissubinterface.update(...)
  * chassis.chassissubinterface.delete(...)
  * chassis.faultsummary.get(...)
  * chassis.instancesummary.get(...)
  * chassis.interfacesummary.get(...)
  * chassis.inventorysummary.get(...)
  * chassis.logicaldevice.create(...)
  * chassis.logicaldevice.get(...)
  * chassis.logicaldevice.update(...)
  * chassis.logicaldevice.delete(...)
  * deployment.pendingchangesrequest.create(...)
  * device.devicerecord.dhcp.ddnssettings.get(...)
  * device.devicerecord.dhcp.ddnssettings.update(...)
  * device.devicerecord.dhcp.dhcprelaysettings.get(...)
  * device.devicerecord.dhcp.dhcprelaysettings.update(...)
  * device.devicerecord.dhcp.dhcpserver.get(...)
  * device.devicerecord.dhcp.dhcpserver.update(...)
  * device.devicerecord.managementconvergencemode.create(...)
  * device.devicerecord.managementconvergencemode.get(...)
  * device.devicerecord.operational.virtualaccessinterface.get(...)
  * health.tunnelstatus.tunneldetails.get(...)
  * integration.cdfmcsnapshot.create(...)
  * integration.cdfmcsnapshot.get(...)
  * integration.refresh_securex_configs(...)
  * job.taskstatus.download_reports(...)
  * object.azureadream.create(...)
  * object.azureadream.get(...)
  * object.azureadream.update(...)
  * object.azureadream.delete(...)
  * object.azureadream.download(...)
  * object.azureadream.usersandgroups(...)
  * object.azureadstatus.get(...)
  * object.ciphersuitelist.create(...)
  * object.ciphersuitelist.get(...)
  * object.customsiiplist.create(...)
  * object.customsiiplist.get(...)
  * object.customsiiplist.update(...)
  * object.customsiiplist.delete(...)
  * object.customsiiplistdownload.get(...)
  * object.customsiurllist.create(...)
  * object.customsiurllist.get(...)
  * object.customsiurllist.update(...)
  * object.customsiurllist.delete(...)
  * object.customsiurllistdownload.get(...)
  * object.distinguishedname.create(...)
  * object.distinguishedname.get(...)
  * object.distinguishednamegroup.get(...)
  * object.externalcacertificate.create(...)
  * object.externalcacertificate.get(...)
  * object.externalcacertificategroup.get(...)
  * object.externalcertificate.create(...)
  * object.externalcertificate.get(...)
  * object.externalcertificategroup.get(...)
  * object.filecategory.get(...)
  * object.filetype.get(...)
  * object.internalcertgroup.get(...)
  * object.networkaddressoverride.get(...)
  * object.ntpserver.create(...)
  * object.ntpserver.get(...)
  * object.ntpserver.update(...)
  * object.ntpserver.delete(...)
  * object.operational.findoverlaps.create(...)
  * object.resourceprofile.create(...)
  * object.resourceprofile.get(...)
  * object.resourceprofile.update(...)
  * object.resourceprofile.delete(...)
  * object.secureclientcustomization.create(...)
  * object.secureclientcustomization.get(...)
  * object.secureclientcustomization.update(...)
  * object.secureclientcustomization.delete(...)
  * object.testazureadream.create(...)
  * policy.chassisplatformsettingspolicy.create(...)
  * policy.chassisplatformsettingspolicy.get(...)
  * policy.chassisplatformsettingspolicy.update(...)
  * policy.chassisplatformsettingspolicy.delete(...)
  * policy.chassisplatformsettingspolicy.accesslistsettings.get(...)
  * policy.chassisplatformsettingspolicy.accesslistsettings.update(...)
  * policy.chassisplatformsettingspolicy.dnssettings.get(...)
  * policy.chassisplatformsettingspolicy.dnssettings.update(...)
  * policy.chassisplatformsettingspolicy.sshclientsettings.get(...)
  * policy.chassisplatformsettingspolicy.sshclientsettings.update(...)
  * policy.chassisplatformsettingspolicy.sshserversettings.get(...)
  * policy.chassisplatformsettingspolicy.sshserversettings.update(...)
  * policy.chassisplatformsettingspolicy.syslogsettings.get(...)
  * policy.chassisplatformsettingspolicy.syslogsettings.update(...)
  * policy.chassisplatformsettingspolicy.timesynchronizationsettings.get(...)
  * policy.chassisplatformsettingspolicy.timesynchronizationsettings.update(...)
  * policy.chassisplatformsettingspolicy.timezonesettings.get(...)
  * policy.chassisplatformsettingspolicy.timezonesettings.update(...)
  * policy.decryptionpolicy.create(...)
  * policy.decryptionpolicy.get(...)
  * policy.decryptionpolicy.update(...)
  * policy.decryptionpolicy.delete(...)
  * policy.decryptionpolicy.decryptionpolicyrule.create(...)
  * policy.decryptionpolicy.decryptionpolicyrule.get(...)
  * policy.decryptionpolicy.decryptionpolicyrule.update(...)
  * policy.decryptionpolicy.decryptionpolicyrule.delete(...)
  * policy.filepolicy.filerule.create(...)
  * policy.filepolicy.filerule.get(...)
  * policy.filepolicy.filerule.update(...)
  * policy.filepolicy.filerule.delete(...)
  * policy.ftdplatformsettingspolicy.httpaccesssettings.get(...)
  * policy.ftdplatformsettingspolicy.httpaccesssettings.update(...)
  * policy.ftdplatformsettingspolicy.netflowpolicies.get(...)
  * policy.ftdplatformsettingspolicy.netflowpolicies.update(...)
  * policy.ftdplatformsettingspolicy.snmpsettings.get(...)
  * policy.ftdplatformsettingspolicy.snmpsettings.update(...)
  * policy.natexemptrule.get(...)
  * policy.ravpn.secureclientcustomizationsettings.get(...)
  * policy.ravpn.secureclientcustomizationsettings.update(...)
  * policy.vpntunnelstatus.get(...)
  * policy.zerotrustpolicy.create(...)
  * policy.zerotrustpolicy.get(...)
  * policy.zerotrustpolicy.update(...)
  * policy.zerotrustpolicy.delete(...)
  * policy.zerotrustpolicy.application.create(...)
  * policy.zerotrustpolicy.application.get(...)
  * policy.zerotrustpolicy.application.update(...)
  * policy.zerotrustpolicy.application.delete(...)
  * policy.zerotrustpolicy.applicationgroup.create(...)
  * policy.zerotrustpolicy.applicationgroup.get(...)
  * policy.zerotrustpolicy.applicationgroup.update(...)
  * policy.zerotrustpolicy.applicationgroup.delete(...)
  * systemconfiguration.changemanagementconfig.get(...)
  * systemconfiguration.changemanagementconfig.update(...)
  * systemconfiguration.remotemanagementaccess.get(...)
  * systemconfiguration.remotemanagementaccess.update(...)
  * troubleshoot.device.create(...)
  * user.users.get(...)

* Added support for FMC 7.3.0 api calls
  * backup.create_device_backup(...)
  * backup.downloadbackup.get(...)
  * backup.file.get(...)
  * backup.file.delete(...)
  * chassis.physicalinterface.get(...)
  * chassis.physicalinterface.update(...)
  * cluster.ftddevicecluster.clusterhealthmonitorsettings.get(...)
  * cluster.ftddevicecluster.clusterhealthmonitorsettings.update(...)
  * device.devicerecord.loopbackinterface.create(...)
  * device.devicerecord.loopbackinterface.get(...)
  * device.devicerecord.loopbackinterface.update(...)
  * device.devicerecord.loopbackinterface.delete(...)
  * device.devicerecord.routing.bfdpolicy.create(...)
  * device.devicerecord.routing.bfdpolicy.get(...)
  * device.devicerecord.routing.bfdpolicy.update(...)
  * device.devicerecord.routing.bfdpolicy.delete(...)
  * device.devicerecord.routing.virtualrouter.bfdpolicy.create(...)
  * device.devicerecord.routing.virtualrouter.bfdpolicy.get(...)
  * device.devicerecord.routing.virtualrouter.bfdpolicy.update(...)
  * device.devicerecord.routing.virtualrouter.bfdpolicy.delete(...)
  * health.csdac.create(...)
  * health.csdac.get(...)
  * health.pathmonitoredinterface.get(...)
  * health.ravpngateway.get(...)
  * health.ravpnsession.get(...)
  * health.ravpnsession.terminate(...)
  * integration.umbrella.datacenter.get(...)
  * integration.umbrella.tunneldeployment.create(...)
  * integration.umbrella.tunneldeployment.get(...)
  * integration.umbrella.tunneldeployment.transcript.get(...)
  * object.bfdtemplate.create(...)
  * object.bfdtemplate.get(...)
  * object.bfdtemplate.update(...)
  * object.bfdtemplate.delete(...)
  * object.dhcpipv6pool.create(...)
  * object.dhcpipv6pool.get(...)
  * object.dhcpipv6pool.update(...)
  * object.dhcpipv6pool.delete(...)
  * object.internalca.create(...)
  * object.internalca.get(...)
  * object.internalca.update(...)
  * object.internalca.delete(...)
  * object.internalca.download(...)
  * object.internalcertificate.create(...)
  * object.internalcertificate.get(...)
  * object.internalcertificate.update(...)
  * object.internalcertificate.delete(...)
  * object.internalcertificate.validate(...)
  * policy.flexconfigpolicy.create(...)
  * policy.flexconfigpolicy.get(...)
  * policy.flexconfigpolicy.migrate(...)
  * policy.ftdplatformsettingspolicy.get(...)
  * policy.ravpn.loadbalancesettings.get(...)
  * policy.ravpn.loadbalancesettings.update(...)

* Completed FMC 7.2.0 api support (previously marked incomplete in 1.1.0)
  * chassis.operational.evaluate_operation(...)
  * deployment.jobhistory.downloadreport.get(...)
  * deployment.jobhistory.emailreport.get(...)
  * device.changemanager(...)
  * device.devicesettings.get(...)
  * device.devicesettings.update(...)
  * device.devicerecord.routing.eigrproute.create(...)
  * device.devicerecord.routing.eigrproute.get(...)
  * device.devicerecord.routing.eigrproute.update(...)
  * device.devicerecord.routing.eigrproute.delete(...)
  * device.devicerecord.routing.virtualrouter.eigrproute.create(...)
  * device.devicerecord.routing.virtualrouter.eigrproute.get(...)
  * device.devicerecord.routing.virtualrouter.eigrproute.update(...)
  * device.devicerecord.routing.virtualrouter.eigrproute.delete(...)
  * integration.ebssnapshot.create(...)
  * integration.ebssnapshot.get(...)
  * integration.testumbrellaconnection.create(...)
  * integration.umbrellaconnection.create(...)
  * integration.umbrellaconnection.get(...)
  * integration.umbrellaconnection.update(...)
  * license.devicelicense.get(...)
  * license.devicelicense.update(...)
  * license.smartlicense.create(...)
  * license.smartlicense.get(...)
  * object.anyconnectexternalbrowserpackage.create(...)
  * object.anyconnectexternalbrowserpackage.get(...)
  * object.anyconnectexternalbrowserpackage.update(...)
  * object.anyconnectexternalbrowserpackage.delete(...)
  * policy.ftdnatpolicy.natrule.delete(...)
  * policy.ftds2svpn.ipseccryptomap.get(...)
  * policy.ftds2svpn.ipseccryptomap.update(...)
  * policy.ftds2svpn.s2svpnsummary.get(...)
  * policy.healthpolicy.get(...)
  * policy.policylock.create(...)
  * policy.policylock.get(...)
  * policy.ravpn.ipsecadvancedsettings.get(...)
  * policy.ravpn.ipsecadvancedsettings.update(...)
  * policy.ravpn.ldapattributemap.get(...)
  * policy.ravpn.ldapattributemap.update(...)
  * policy.umbrelladnspolicy.create(...)
  * policy.umbrelladnspolicy.get(...)
  * policy.umbrelladnspolicy.update(...)
  * policy.umbrelladnspolicy.delete(...)
  * policy.umbrelladnspolicy.umbrelladnsrule.get(...)
  * policy.umbrelladnspolicy.umbrelladnsrule.update(...)
  * troubleshoot.task.create(...)
  * update.snapshot(...)

## Documentation

* Migrated documentation from Sphinx to MkDocs with Material theme and mkdocstrings.
* Added Google-style docstrings to all 312 resource classes, sourced from the FMC OAS3 specs
  (7.2.5, 7.3.1, 7.4.2). Each docstring includes description, tags, supported operations,
  operation IDs, and query parameters.
* API reference pages are now auto-generated at build time from the codebase via
  `mkdocs-gen-files` and `mkdocs-literate-nav`. Adding a new resource class automatically
  includes it in the docs without any manual file edits.
* Added FMC API release constants for 7.6.0, 7.7.0, and 10.0.0 in `defaults.py`.

## Fixed

* Fixed `policy.accesspolicy.operational.hitcounts.delete()` not accepting `container_uuid`, `device_id`, or `ids` parameters, making it impossible to reset hitcounts (Issue #102).
* Fixed `TypeError` in `netmap.host.delete()` and `netmap.vulnerability.delete()` caused by unsupported `url=` keyword argument to `Resource.delete()`.
* Fixed `cluster.ftddevicecluster.operational.command()` building malformed URLs.
* Fixed `chassis.operational` methods building malformed URLs.
* Fixed `health.tunnelsummary` `PATH` pointing to `/health/metrics/{uuid}` instead of `/health/tunnelsummaries/{uuid}`.
* Fixed `policy.networkanalysispolicy.inspectorconfig` `CONTAINER_PATH` pointing to `intrusionpolicies` instead of `networkanalysispolicies`.
* Fixed `policy.prefilterpolicy.defaultaction` `CONTAINER_NAME` set to `'AccessPolicy'` instead of `'PrefilterPolicy'`.
* Fixed `policy.ftds2svpn.endpoint` `CONTAINER_NAME` set to `'Endpoint'` instead of `'FtdS2sVpn'`.
* Fixed `mapping.PARAMS` missing `group_dependency` and `hostname` entries causing `KeyError` in `support_params` decorator.
* Fixed `device.devicerecord.operational.command.get()` passing a plain dict to `utils.search_filter()` where a list is expected.
* Fixed `policy.accesspolicy.loggingsettings` not instantiated in `AccessPolicy.__init__()`.
* Fixed `policy.identitypolicy` not instantiated in `Policy.__init__()`.
* Fixed `object.standardaccesslist` missing `MINIMUM_VERSION_REQUIRED_CREATE/UPDATE/DELETE` constants.
* Fixed missing `ospfv3route` and `ospfv3interface` modules under `virtualrouter`.
* Fixed `object.communitylist` missing `MINIMUM_VERSION_REQUIRED_CREATE/UPDATE/DELETE` constants.
* Fixed `policy.ravpn` not instantiated in `Policy.__init__()`.
* Fixed `update.revert()` incorrectly named `retry`, shadowing the existing `retry()` method.

# 1.2.4 [2026-01-14]

## Fixed

* Security Cloud Control failed authentication changed message handling
* Bump dependecies version

# 1.2.3 [2025-07-02]

## New

* Handle authentication token refresh errors and re-authenticate if necessary

# 1.2.2 [2025-06-24]

## Fixed

* Bump dependent libriaries versions

# 1.2.1 [2025-03-26]

## Fixed

* Bulk updates fail for UPDATE operations (Issue #71)

# 1.2.0 [2025-02-17]

## New

* Add support for Cloud Delivered FMC (cdFMC) (#79, #80)
* Add helper function `get_domain_name` (#74)

## Fixed

* Missing filtering support for Network Group (#81)
* Corrected API Endpoint for `auditrecords` (#67)
* Ensure version response contains processable information (#77)
* Standard community fix (#78)
* Missing RaVPN policy hook
* Other minor fixes

# 1.1.0 [2023-03-19]

## New

* Added support for FMC 7.2.0 api calls (incomplete)
  * object.anyconnectpackage.create(...)
  * object.anyconnectpackage.update(...)
  * object.anyconnectpackage.delete(...)
  * object.anyconnectprofile.create(...)
  * object.anyconnectprofile.update(...)
  * object.anyconnectprofile.delete(...)
  * object.certenrollment.create(...)
  * object.certenrollment.update(...)
  * object.certenrollment.delete(...)
  * object.certificatemap.create(...)
  * object.certificatemap.update(...)
  * object.certificatemap.delete(...)
  * object.grouppolicy.create(...)
  * object.grouppolicy.update(...)
  * object.grouppolicy.delete(...)
  * object.hostscanpackage.create(...)
  * object.hostscanpackage.update(...)
  * object.hostscanpackage.delete(...)
  * object.ipv4addresspool.create(...)
  * object.ipv4addresspool.update(...)
  * object.ipv4addresspool.delete(...)
  * object.ipv6addresspool.create(...)
  * object.ipv6addresspool.update(...)
  * object.ipv6addresspool.delete(...)
  * object.radiusservergroup.create(...)
  * object.radiusservergroup.update(...)
  * object.radiusservergroup.delete(...)
  * object.ssoserver.create(...)
  * object.ssoserver.update(...)
  * object.ssoserver.delete(...)
  * policy.ravpn.create(...)
  * policy.ravpn.update(...)
  * policy.ravpn.delete(...)
  * policy.ravpn.addressassignmentsettings.update(...)
  * policy.ravpn.certificatemapsettings.update(...)
  * policy.ravpn.connectionprofile.create(...)
  * policy.ravpn.connectionprofile.update(...)
  * policy.ravpn.connectionprofile.delete(...)


* Added support for FMC 7.1.0 api calls
  * chassis.get(...)
  * chassis.networkmodule.update(...)
  * chassis.networkmodule.get(...)
  * chassis.interface.get(...)
  * chassis.interface.evaluate_operation(...)
  * chassis.operational.sync_networkmodule(...)
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
  * object.standardcommunitylist.update(...)
  * object.standardcommunitylist.delete(...)
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

* Added support for pre 7.1 api calls that were still missing
  * cluster.ftddevicecluster.create(...)
  * cluster.ftddevicecluster.update(...)
  * cluster.ftddevicecluster.delete(...)
  * device.devicerecord.routing.virtualrouter.ipv4staticroute.create(...)
  * device.devicerecord.routing.virtualrouter.ipv4staticroute.get(...)
  * device.devicerecord.routing.virtualrouter.ipv4staticroute.update(...)
  * device.devicerecord.routing.virtualrouter.ipv4staticroute.delete(...)
  * device.devicerecord.routing.virtualrouter.ipv6staticroute.create(...)
  * device.devicerecord.routing.virtualrouter.ipv6staticroute.get(...)
  * device.devicerecord.routing.virtualrouter.ipv6staticroute.update(...)
  * device.devicerecord.routing.virtualrouter.ipv6staticroute.delete(...)
  * device.devicerecord.routing.virtualrouter.ospfv2route.get(...)
  * device.devicerecord.routing.virtualrouter.ospfv2interface.get(...)
  * device.devicerecord.routing.virtualrouter.ospfv3route.get(...)
  * device.devicerecord.routing.virtualrouter.ospfv3interface.get(...)

## Fixed

* missing filtering support for health.alert
* missing filtering support for health.metric

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
  * GET object.usage
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
  * GET policy.ravpn.addressassignmentsettings
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
