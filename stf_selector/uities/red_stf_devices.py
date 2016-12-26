#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Contains the : class: 'http_stf'"""
import requests
import logging
import json
import yaml
from constant import BASE_URL

logger = logging.getLogger(__name__)


class http_stf(object):
    """
    Use this module to get devices of remote stf platform
    """

    def __init__(self):
        pass

    def get_devices(self, url=BASE_URL, headers=None):
        """
        Send request to stf and get devices

        :param url: the address of stf platform
        :type url: str
        :param headers: headers which used to login in stf
        like : {Authorization:'Bearer ...."}
        :type headers:dict
        :return: if 'success' is True, return list of devices, instead
        of the response 'success' is False, return None.
        """
        # url = BASE_URL
        # if need try catch
        response = requests.get(url, headers=headers)
        res = response.json()
        if res is not None and res["success"] is True:
            # unicode to str
            return yaml.safe_load(json.dumps(res))
        else:
            logger.info("Request error:" + str(res))
            return None


if __name__ == '__main__':
    # print http_stf().get_devices
    headers = {"Authorization": 'Bearer 3e5dd447cd334d549c849d19707eb269df74cabd67e5400986a5240023af6421'}
    print http_stf().get_devices(headers=headers)
