#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tinydb import TinyDB
from tinydb.storages import MemoryStorage, JSONStorage


class DB(TinyDB):
    # To modify the default storage for all TinyDB instances
    TinyDB.DEFAULT_STORAGE = MemoryStorage
    pass


class MemStroage(MemoryStorage):
    pass


class JsonStorage(JSONStorage):
    pass
