# -*- coding: utf-8 -*-
"""
stf devices stf_selector

some fields we often use
===============================================
field	     e.g.
manufacturer OPPO
version      5.1.1
display	     {height:1920，width:1080}
sdk	         22
serial	     778d4f10
platform	 android
mode         Plusm A
....         ...
===============================================
"""

import logging

from stf import STF
from query import where
from tinydb import TinyDB
from tinydb.storages import MemoryStorage, JSONStorage

logger = logging.getLogger(__name__)

TinyDB.DEFAULT_STORAGE = MemoryStorage


class Selector(object):
    """
    According to users requirements to select devices
    """

    def __init__(self, url=None, token=None):
        """
        Construct method
        """
        self._db = TinyDB(storage=MemoryStorage)
        self._url = url
        self._token = token

    def load(self):
        """
        Use the data which got from stf platform to crate query db

        :return: the len of records in the db's table
        """
        res = STF().devices(url=self._url, token=self._token)
        if res is not None:
            list_devices = res['devices']
            eids = self._db.insert_multiple(list_devices)
            return len(eids)
        else:
            return 0

    def find(self, cond=None):
        """
        According condition to filter devices and return
        :param cond: condition to filter devices
        :type cond: where
        :return: stf_selector object and its db contains devices
        """
        if cond is not None:
            res = self._db.search(cond)
            self.purge()
            self._db.insert_multiple(res)
        return self

    def devices(self):
        """
        return all devices that meeting the requirement
        :return: list of devices
        """
        return self._db.all()

    def refresh(self):
        """
        reload the devices info from stf
        :return: the len of records in the db's table
        """
        self.purge()
        return self.load()

    def count(self):
        """
        count the records in the db's table
        :return: the len of records in the db's table
        """
        return len(self._db.all())

    def purge(self):
        """
        remove all the data from the db
        :return:
        """
        self._db.purge()


if __name__ == '__main__':
    url = "http://10.12.144.16:7100/api/v1/devices"
    token = '3e5dd447cd334d549c849d19707eb269df74cabd67e5400986a5240023af6421'
    selector = Selector(url=url, token=token)
    selector.load()
    selector = selector.find(
        cond=((where("manufacturer") == 'OPPO')
              | (where("manufacturer") == 'SAMSUNG'))
             & (where("sdk") == '19')
             & (where("display")["height"] == 1920)) \
        .find(cond=where("display")["width"] == 1080)
    print selector.devices()
