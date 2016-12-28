#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Contains the : class: 'STF'"""
import requests
import logging
import json
import yaml

logger = logging.getLogger(__name__)


class STF(object):
    """
    Use this module to get devices from remote stf platform
    """

    def __init__(self):
        pass

    def devices(self, url=None, token=None):
        """
        Send request to stf and get devices

        :param url: the address of stf platform
        :type url: str
        :param token: token which used to login in stf
        like : '3e5dd447cd334d549c849d19707eb269df74cabd67......'
        :type token: dict
        :return: if 'success' is True, return list of devices.
        Otherwise, return None.
        """
        if url is None:
            logger.info("Please set the request address!")
            return None
        if token is not None:
            auth = dict()
            auth["Authorization"] = 'Bearer ' + token
            auth = auth
        response = requests.get(url=url, headers=auth)
        res = response.json()
        if res is not None and res["success"] is True:
            return yaml.safe_load(json.dumps(res))  # unicode to str
        else:
            logger.info("stf response false:" + str(res))
            return None
