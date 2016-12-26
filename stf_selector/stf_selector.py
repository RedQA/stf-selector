# -*- coding: utf-8 -*-
"""
stf devices selector
===============================================
field	     e.g.
manufacturer OPPO
version      5.1.1
display	     {height:1920，width:1080}
sdk	         22
serial	     778d4f10
platform	 android
mode         Plusm A
===============================================
"""

from tinydb import TinyDB, Query, where
from tinydb.storages import MemoryStorage
from uities.red_stf_devices import http_stf
import logging

logger = logging.getLogger(__name__)

# To modify the default storage for all TinyDB instances
TinyDB.DEFAULT_STORAGE = MemoryStorage
DEFAULT_TABLE = "stf_device_selector"


class stf_selector(object):
    """
    According to users requirements to select devices
    """

    def __init__(self):
        """
        Construct method
        """
        self.db = TinyDB(storage=MemoryStorage, default_table=DEFAULT_TABLE)

    def insert_data(self, headers):
        """
        Use the data which got from stf platform to crate query db

        :return: table contains devices info
        """
        res = http_stf().get_devices(headers=headers)
        if res is None:
            pass
        else:
            list_devices = res['devices']
            self.db.insert_multiple(list_devices)

    def devices_selector(self, use=False, number=0, **kwargs):
        """
        According to cond to select devices

        :param number: the number of mobile phone to need
        :type number: int
        :param kwargs: cond ,like Query('sdk') == '22'
        or multi cond (('Query('sdk') == '22') & ('Query('manufacturer')=='OPPO'))
        or (('Query('sdk') == '22') | ('Query('manufacturer')=='OPPO')
        :return: res that contains required devices "adb remote connect address",  type(res) is list
        """
        # conditions of defaults
        temp = (where("display").exists())
        temp &= (where("present").exists())
        temp &= (where("using").exists())
        temp &= (where("present") == True)
        if use is True:
            temp &= (where("using") == True)
        else:
            temp &= (where("using") == False)
        # conditions of user
        for k, v in kwargs.items():
            if type(v) is dict:
                for x, y in v.items():
                    temp &= (Query([k,x]) == y)
            else:
                temp &= (where(k) == v)
        res = self.db.search(temp)
        un_use_devices = []
        if res is not None and len(res) >= number:
            temp = {}
            for device in res:
                if device.get('remoteConnectUrl') is not None:
                    temp['url'] = device['remoteConnectUrl']
                else:
                    temp['url'] = device['display']['url'][5:]
                temp['version'] = device['version']
                un_use_devices.insert(0, temp)
        return un_use_devices


if __name__ == '__main__':
    stf_selector = stf_selector()
    headers = {"Authorization": 'Bearer 3e5dd447cd334d549c849d19707eb269df74cabd67e5400986a5240023af6421'}
    stf_selector.insert_data(headers)
    # print stf_selector.db.all()
    print stf_selector.devices_selector(manufacturer='OPPO', sdk='19', display={"height": 1920, "width": 1080})
