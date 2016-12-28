#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_stf_selector
----------------------------------

Tests for `stf_selector` module.
"""

from mock import patch
from stf_selector.stf import STF
from stf_selector.query import where
from stf_selector.selector import Selector


@patch.object(STF, 'devices')
def test_find_without_cond(mock_devices, generate_data):
    """
    test find method with no cond
    :return: len of devices
    """
    mock_devices.return_value = generate_data
    s = Selector()
    s.load()
    s = s.find()
    assert s.count() == 9


@patch.object(STF, 'devices')
def test_find_with_one_cond(mock_devices, generate_data):
    """
    test find method with one cond

    :param cond: condition to filter devices.
        like : where("sdk")==19 the details syntax
    See more at: http://
    :type cond:  where
    :return: len of device
    """
    mock_devices.return_value = generate_data
    s = Selector()
    s.load()

    cond = where("sdk") == '19'
    s = s.find(cond=cond)
    assert s.count() == 2


@patch.object(STF, 'devices')
def test_find_with_multi_conds(mock_devices, generate_data):
    """
    test find method with multi cond

    condition to filter devices.
    there are two ways to do muitl filter
    Firstly:
        like : (where("sdk")==19) & (where("manufacturer") == 'OPPO')
        like : (where("sdk")==19) | (where("manufacturer") == 'OPPO')
        or like :((where("manufacturer") == 'SAMSUNG') | (where("manufacturer") == 'OPPO')) & (where("sdk")==19)
    Secondly:
        s.find(cond=cond).find(cond=cond)
        or : s.find(cond=cond).find(cond=cond).find(...)
    See more at: http://
    :type : where
    :return: len of device
    """
    mock_devices.return_value = generate_data
    s = Selector()
    s.load()

    # you can code like
    cond = ((where("manufacturer") == 'SAMSUNG')
            | (where("manufacturer") == 'OPPO')) \
           & (where("sdk") == '19')
    s = s.find(cond=cond)
    assert s.count() == 1
