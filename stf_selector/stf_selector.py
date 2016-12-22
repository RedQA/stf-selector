# -*- coding: utf-8 -*-
"""
stf devices selector
===============================================
维度	    字段	         e.g.	备注
设备商	manufacturer OPPO
版本	    version      5.1.1
屏幕尺寸	display	     {height:1920，width:1080}
SDK版本	sdk	22
设备序列  serial	     778d4f10
系统平台	platform	 android
设备型号	mode         Plusm A
===============================================
"""

from tinydb import TinyDB, Query, where
from tinydb.storages import MemoryStorage
from uities.red_stf_devices import HTTP_STF

# To modify the default storage for all TinyDB instances
TinyDB.DEFAULT_STORAGE = MemoryStorage


class stf_selector(object):
    """
    According users requirements to select devices
    """

    def __init__(self):
        """
        Construct method
        """
        self.db = TinyDB(storage=MemoryStorage)
        self.table = self.db.table(name="stf_device_selector")

    def create_tables(self):
        """
        Use the data which got from stf platform to crate query table
        :return:
        """
        dict = HTTP_STF().get()
        self.table.insert(dict)


    def devices_selector(self, *args, **kwargs):
        pass
        # query = Query()
        # return self.db.contains(query[u'success']==True)

if __name__ == '__main__':
    stf_selector = stf_selector()
    stf_selector.create_tables()
    print stf_selector.devices_selector()
