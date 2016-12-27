#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_stf_selector
----------------------------------

Tests for `stf_selector` module.
"""

import pytest

from click.testing import CliRunner
from stf_selector.uities.log import LOGGER
from stf_selector import cli
from tinydb import Query, where
from stf_selector.uities.constant import BASE_URL, AUTH_HEADER
from stf_selector.stf_selector import selector

LOGGER.info("*********Begin**********")


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
    s = selector()
    url = BASE_URL
    headers = AUTH_HEADER
    s.insert_data(url, headers)
    s = s.find()
    print s.get_devices()


def test_find_with_one_cond(cond):
    """
    test find method with one cond
    Firstly, you need do two change :
    a）configure BASE_URL in constant.py
        according to your real address of stf
    b) configure headers to your authorization

    :param cond: condition to filter devices.
        like : Query("sdk")==19 the details syntax
    See more at: http://tinydb.readthedocs.io/en/latest/usage.html
    :type cond: Query or Where
    :return: list of device
    """
    s = selector()
    url = BASE_URL
    headers = AUTH_HEADER
    s.insert_data(url, headers)
    cond = (Query("sdk") == 19)
    s = s.find(cond=cond)
    print s.get_devices()


def test_find_with_multi_conds(cond):
    """
    test find method with multi cond
    Firstly, you need do two change :
    a）configure BASE_URL in constant.py
        according to your real address of stf
    b) configure headers to your authorization

    :param cond: condition to filter devices.
    there are two ways to do muitl filter
    Firstly:
        like : (Query("sdk")==19) & (Query("manufacturer") == 'OPPO')
        like : (Query("sdk")==19) | (Query("manufacturer") == 'OPPO')
        or like :((Query("manufacturer") == 'SAMSUNG') | (Query("manufacturer") == 'OPPO')) & (Query("sdk")==19)
    Secondly:
        s = selector()
        url = BASE_URL
        headers = AUTH_HEADER
        s.insert_data(url, headers)
        s.find(cond=cond).find(cond=cond)
        or : s.find(cond=cond).find(op="|",cond=cond).find(...)
    See more at: http://tinydb.readthedocs.io/en/latest/usage.html
    :type cond: Query or Where
    :return: list of device
    """
    s = selector()
    url = BASE_URL
    headers = AUTH_HEADER
    s.insert_data(url, headers)

    # you can code like
    cond = ((Query("manufacturer") == 'SAMSUNG')
            | (Query("manufacturer") == 'OPPO')) & (Query("sdk") == 19)
    s = s.find(cond=cond)

    # or like
    # s.find((Query("manufacturer") == 'SAMSUNG')
    #         | (Query("manufacturer") == 'OPPO')).find((Query("sdk") == 19))
    print s.get_devices()
