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

TinyDB.DEFAULT_STORAGE = MemoryStorage


class stf_selector(object):
    """
    According users requirements to select devices
    """
    db = TinyDB(storage=MemoryStorage)

    def __init__(self):
        """
        Construct method
        """
        pass

    def create_tables(self):
        """
        Use the data which got from stf platform to crate query table
        :return:
        """
        pass
