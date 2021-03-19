# -*- coding: utf-8 -*-

from fireREST.fmc.update.upgradepackage import UpgradePackage


def test_initialization(fmc):
    upgradepackage = fmc.update.upgradepackage
    assert isinstance(upgradepackage, UpgradePackage)


def test_get_upgradepackages(fmc):
    actual_result = fmc.update.upgradepackage.get()

    assert type(actual_result) in (dict, list)
