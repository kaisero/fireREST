# -*- coding: utf-8 -*-

from fireREST.fmc.policy.accesspolicy import AccessPolicy
from fireREST.fmc.policy.filepolicy import FilePolicy
from fireREST.fmc.policy.ftdnatpolicy import FtdNatPolicy
from fireREST.fmc.policy.ftds2svpn import FtdS2sVpn
from fireREST.fmc.policy.intrusionpolicy import IntrusionPolicy
from fireREST.fmc.policy.prefilterpolicy import PrefilterPolicy
from fireREST.fmc.policy.snmpalert import SnmpAlert
from fireREST.fmc.policy.syslogalert import SyslogAlert


def test_initialization(fmc):
    assert isinstance(fmc.policy.accesspolicy, AccessPolicy)
    assert isinstance(fmc.policy.filepolicy, FilePolicy)
    assert isinstance(fmc.policy.ftdnatpolicy, FtdNatPolicy)
    assert isinstance(fmc.policy.ftds2svpn, FtdS2sVpn)
    assert isinstance(fmc.policy.intrusionpolicy, IntrusionPolicy)
    assert isinstance(fmc.policy.prefilterpolicy, PrefilterPolicy)
    assert isinstance(fmc.policy.snmpalert, SnmpAlert)
    assert isinstance(fmc.policy.syslogalert, SyslogAlert)
