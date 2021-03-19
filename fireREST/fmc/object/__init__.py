from fireREST.fmc import Connection, Resource
from fireREST.fmc.object.anyprotocolportobject import AnyProtocolPortObject
from fireREST.fmc.object.application import Application
from fireREST.fmc.object.applicationcategory import ApplicationCategory
from fireREST.fmc.object.applicationfilter import ApplicationFilter
from fireREST.fmc.object.applicationproductivities import ApplicationProductivity
from fireREST.fmc.object.applicationrisk import ApplicationRisk
from fireREST.fmc.object.applicationtag import ApplicationTag
from fireREST.fmc.object.applicationtype import ApplicationType
from fireREST.fmc.object.aspathlist import AsPathList
from fireREST.fmc.object.certenrollment import CertEnrollment
from fireREST.fmc.object.communitylist import CommunityList
from fireREST.fmc.object.continent import Continent
from fireREST.fmc.object.country import Country
from fireREST.fmc.object.dnsservergroup import DnsServerGroup
from fireREST.fmc.object.endpointdevicetype import EndpointDeviceType
from fireREST.fmc.object.expandedcommunitylist import ExpandedCommunityList
from fireREST.fmc.object.extendedaccesslist import ExtendedAccessList
from fireREST.fmc.object.fqdn import Fqdn
from fireREST.fmc.object.geolocation import GeoLocation
from fireREST.fmc.object.globaltimezone import GlobalTimeZone
from fireREST.fmc.object.host import Host
from fireREST.fmc.object.icmpv4object import Icmpv4Object
from fireREST.fmc.object.icmpv6object import Icmpv6Object
from fireREST.fmc.object.ikev1ipsecproposal import Ikev1IpsecProposal
from fireREST.fmc.object.ikev1policy import Ikev1Policy
from fireREST.fmc.object.ikev2ipsecproposal import Ikev2IpsecProposal
from fireREST.fmc.object.ikev2policy import Ikev2Policy
from fireREST.fmc.object.interface import Interface
from fireREST.fmc.object.interfacegroup import InterfaceGroup
from fireREST.fmc.object.ipv4prefixlist import Ipv4PrefixList
from fireREST.fmc.object.ipv6prefixlist import Ipv6PrefixList
from fireREST.fmc.object.isesecuritygrouptag import IseSecurityGroupTag
from fireREST.fmc.object.keychain import KeyChain
from fireREST.fmc.object.network import Network
from fireREST.fmc.object.networkaddress import NetworkAddress
from fireREST.fmc.object.networkgroup import NetworkGroup
from fireREST.fmc.object.policylist import PolicyList
from fireREST.fmc.object.port import Port
from fireREST.fmc.object.portobjectgroup import PortObjectGroup
from fireREST.fmc.object.protocolportobject import ProtocolPortObject
from fireREST.fmc.object.range import Range
from fireREST.fmc.object.realmuser import RealmUser
from fireREST.fmc.object.realmusergroup import RealmUserGroup
from fireREST.fmc.object.routemap import RouteMap
from fireREST.fmc.object.securitygrouptag import SecurityGroupTag
from fireREST.fmc.object.securityzone import SecurityZone
from fireREST.fmc.object.siurlfeed import SiUrlFeed
from fireREST.fmc.object.siurllist import SiUrlList
from fireREST.fmc.object.slamonitor import SlaMonitor
from fireREST.fmc.object.standardaccesslist import StandardAccessList
from fireREST.fmc.object.standardcommunitylist import StandardCommunityList
from fireREST.fmc.object.timerange import Timerange
from fireREST.fmc.object.timezone import Timezone
from fireREST.fmc.object.tunneltag import TunnelTag
from fireREST.fmc.object.url import Url
from fireREST.fmc.object.urlcategory import UrlCategory
from fireREST.fmc.object.urlgroup import UrlGroup
from fireREST.fmc.object.variableset import VariableSet
from fireREST.fmc.object.vlangrouptag import VlanGroupTag
from fireREST.fmc.object.vlantag import VlanTag


class Object:
    def __init__(self, conn: Connection):
        self.anyprotocolportobject = AnyProtocolPortObject(conn)
        self.application = Application(conn)
        self.applicationcategory = ApplicationCategory(conn)
        self.applicationfilter = ApplicationFilter(conn)
        self.applicationproductivities = ApplicationProductivity(conn)
        self.applicationrisk = ApplicationRisk(conn)
        self.applicationtag = ApplicationTag(conn)
        self.applicationtype = ApplicationType(conn)
        self.aspathlist = AsPathList(conn)
        self.certenrollment = CertEnrollment(conn)
        self.communitylist = CommunityList(conn)
        self.continent = Continent(conn)
        self.country = Country(conn)
        self.dnsservergroup = DnsServerGroup(conn)
        self.endpointdevicetype = EndpointDeviceType(conn)
        self.expandedcommunitylist = ExpandedCommunityList(conn)
        self.extendedaccesslist = ExtendedAccessList(conn)
        self.fqdn = Fqdn(conn)
        self.geolocation = GeoLocation(conn)
        self.globaltimezone = GlobalTimeZone(conn)
        self.host = Host(conn)
        self.icmpv4object = Icmpv4Object(conn)
        self.icmpv6object = Icmpv6Object(conn)
        self.ikev1ipsecproposal = Ikev1IpsecProposal(conn)
        self.ikev1policy = Ikev1Policy(conn)
        self.ikev2ipsecproposal = Ikev2IpsecProposal(conn)
        self.ikev2policy = Ikev2Policy(conn)
        self.interface = Interface(conn)
        self.interfacegroup = InterfaceGroup(conn)
        self.ipv4prefixlist = Ipv4PrefixList(conn)
        self.ipv6prefixlist = Ipv6PrefixList(conn)
        self.isesecuritygrouptag = IseSecurityGroupTag(conn)
        self.keychain = KeyChain(conn)
        self.network = Network(conn)
        self.networkaddress = NetworkAddress(conn)
        self.networkgroup = NetworkGroup(conn)
        self.policylist = PolicyList(conn)
        self.port = Port(conn)
        self.portobjectgroup = PortObjectGroup(conn)
        self.protocolportobject = ProtocolPortObject(conn)
        self.range = Range(conn)
        self.realmuser = RealmUser(conn)
        self.realmusergroup = RealmUserGroup(conn)
        self.routemap = RouteMap(conn)
        self.securitygrouptag = SecurityGroupTag(conn)
        self.securityzone = SecurityZone(conn)
        self.siurlfeed = SiUrlFeed(conn)
        self.siurllist = SiUrlList(conn)
        self.slamonitor = SlaMonitor(conn)
        self.standardaccesslist = StandardAccessList(conn)
        self.standardcommunitylist = StandardCommunityList(conn)
        self.timerange = Timerange(conn)
        self.timezone = Timezone(conn)
        self.tunneltag = TunnelTag(conn)
        self.url = Url(conn)
        self.urlcategory = UrlCategory(conn)
        self.urlgroup = UrlGroup(conn)
        self.variableset = VariableSet(conn)
        self.vlangrouptag = VlanGroupTag(conn)
        self.vlantag = VlanTag(conn)
