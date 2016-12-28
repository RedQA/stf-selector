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

    def devices(self, url=None, headers=None):
        """
        Send request to stf and get devices

        :param url: the address of stf platform
        :type url: str
        :param headers: headers which used to login in stf
        like : {Authorization:'Bearer ....'}
        :type headers: dict
        :return: if 'success' is True, return list of devices.
        Otherwise, return None.
        """
        if url is None:
            logger.info("Please set the request address!")
            return None
        response = requests.get(url=url, headers=headers)
        res = response.json()
        if res is not None and res["success"] is True:
            return yaml.safe_load(json.dumps(res))  # unicode to str
        else:
            logger.info("stf response false:" + str(res))
            return None


if __name__ == '__main__':
    # no url or headers
    print STF().devices()
    # url and no headers
    url = "http://10.12.144.16:7100/api/v1/devices"
    print STF().devices()
    # with url and headers
    headers = {"Authorization": 'Bearer 3e5dd447cd334d549c849d19707eb269df74cabd67e5400986a5240023af6421'}
    print STF().devices(url=url, headers=headers)
