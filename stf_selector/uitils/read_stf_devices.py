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
        # return res
        # print res
        un_use_list = []
        in_use_list = []
        no_url_list = []
        disconnect_list = []
        for device in res['devices']:
            if device.get('display') is not None:
                temp = {}
                if device.get('remoteConnectUrl') is not None:
                    temp['url'] = device['remoteConnectUrl']
                else:
                    temp['url'] = device['display']['url'][5:]
                temp['version'] = device['version']
                if device['present'] is True:
                    if device['using'] is True:
                        in_use_list.insert(0, temp)
                    else:
                        un_use_list.insert(0, temp)
                else:
                    # disconnect list
                    disconnect_list.insert(0, temp)
            else:
                no_url_list.insert(0,  device['serial'])
        return un_use_list, in_use_list, no_url_list, disconnect_list


if __name__ == '__main__':
    un_use_list = HTTP_STF().get()[0]
    print un_use_list
    for device in un_use_list:
        print device['url'][:-5], device['url'][-4:]
