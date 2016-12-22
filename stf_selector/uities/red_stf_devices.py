#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""本模块主要用来封装对stf的request按到response处理"""
import requests
import logging

logger = logging.getLogger(__name__)


class HTTP_STF(object):
    """处理对stf模块的请求和处理"""

    BASE_URL = 'http://10.12.144.16:7100/api/v1/devices'

    def __init__(self):
        pass

    def get(self, url=BASE_URL, params=None, **kwargs):
        """
        发送get请求
        """
        headers = {'Authorization': 'Bearer 3e5dd447cd334d549c849d19707eb269df74cabd67e5400986a5240023af6421'}
        response = requests.get(url, headers=headers)
        # print response.content
        res = response.json()
        return res


if __name__ == '__main__':
    HTTP_STF().get()
