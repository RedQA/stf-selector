#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_stf_selector
----------------------------------

Tests for `stf_selector` module.
"""

import pytest

from click.testing import CliRunner
from stf_selector import cli
from stf_selector.where import where
from stf_selector.stf_selector import Selector


@pytest.fixture
def response():
    """
    Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """
    Sample pytest test function with the pytest fixture as an argument.
    """
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
    print "test"


def test_command_line_interface():
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'stf_selector.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output


def test_find_with_cond():
    """
    test find method with no cond
    Firstly, you need do two change :
    a）configure BASE_URL in constant.py
        according to your real address of stf
    b) configure headers to your authorization

    :return: list of device
    """
    url = "http://10.12.144.16:7100/api/v1/devices"
    headers = {"Authorization": 'Bearer 3e5dd447cd334d549c849d19707eb269df74cabd67e5400986a5240023af6421'}
    s = Selector(url=url, headers=headers)
    s.load()
    s = s.find()
    print s.devices()
    print "--------0------"


def test_find_with_one_cond():
    """
    test find method with one cond
    Firstly, you need do two change :
    a）configure BASE_URL in constant.py
        according to your real address of stf
    b) configure headers to your authorization

    :param cond: condition to filter devices.
        like : where("sdk")==19 the details syntax
    See more at: http://
    :type cond:  where
    :return: list of device
    """
    url = "http://10.12.144.16:7100/api/v1/devices"
    headers = {"Authorization": 'Bearer 3e5dd447cd334d549c849d19707eb269df74cabd67e5400986a5240023af6421'}
    s = Selector(url=url, headers=headers)
    s.load()
    cond = where("sdk") == '19'
    s = s.find(cond=cond)
    print s.devices()
    print "--------1------"


def test_find_with_multi_conds():
    """
    test find method with multi cond
    Firstly, you need do two change :
    a）configure BASE_URL in constant.py
        according to your real address of stf
    b) configure headers to your authorization

    :param cond: condition to filter devices.
    there are two ways to do muitl filter
    Firstly:
        like : (where("sdk")==19) & (where("manufacturer") == 'OPPO')
        like : (where("sdk")==19) | (where("manufacturer") == 'OPPO')
        or like :((where("manufacturer") == 'SAMSUNG') | (where("manufacturer") == 'OPPO')) & (where("sdk")==19)
    Secondly:
        s = selector()
        url = BASE_URL
        headers = AUTH_HEADER
        s.insert_data(url, headers)
        s.find(cond=cond).find(cond=cond)
        or : s.find(cond=cond).find(op="|",cond=cond).find(...)
    See more at: http://
    :type cond: where
    :return: list of device
    """
    url = "http://10.12.144.16:7100/api/v1/devices"
    headers = {"Authorization": 'Bearer 3e5dd447cd334d549c849d19707eb269df74cabd67e5400986a5240023af6421'}
    s = Selector(url=url, headers=headers)
    s.load()

    # you can code like
    cond = ((where("manufacturer") == 'SAMSUNG')
            | (where("manufacturer") == 'OPPO')) \
           & (where("sdk") == '19')
    s = s.find(cond=cond)

    # or like
    # s.find((where("manufacturer") == 'SAMSUNG')
    #         | (where("manufacturer") == 'OPPO')).find((where("sdk") == 19))
    print s.devices()
    print "--------2------"
