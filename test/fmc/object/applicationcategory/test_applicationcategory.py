# -*- coding: utf-8 -*-
from fireREST.fmc.object.applicationcategory import ApplicationCategory


def test_initialization(fmc):
    obj = fmc.object
    assert isinstance(obj.applicationcategory, ApplicationCategory)


def test_get_applicationcategory_objects(fmc):
    actual_result = fmc.object.applicationcategory.get()

    assert len(actual_result) > 0


def test_get_applicationcategory_by_name(fmc):
    expected_result = 'active directory'
    actual_result = fmc.object.applicationcategory.get(name=expected_result)['name']

    assert expected_result == actual_result


def test_get_applicationcategory_by_id(fmc):
    expected_result = fmc.object.applicationcategory.get()[0]['id']
    actual_result = fmc.object.applicationcategory.get(uuid=expected_result)['id']

    assert expected_result == actual_result
