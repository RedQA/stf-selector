#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tinydb import Query


def where(key):
    return Query([key])
