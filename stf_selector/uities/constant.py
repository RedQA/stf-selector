#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging

logger = logging.getLogger(__name__)

# 项目路径抽象
PROJECT_PATH = os.path.abspath(
    os.path.join(__file__, os.path.pardir,
                 os.path.pardir, os.path.pardir))

RESOURCE_PATH = os.path.join(PROJECT_PATH, "resources")

# Andorid package 名字
BASE_URL = 'http://10.12.144.16:7100/api/v1/devices'
