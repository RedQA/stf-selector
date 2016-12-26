# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""logger"""

import os
import logging.config
import yaml

from constant import PROJECT_PATH, RESOURCE_PATH

_LOG_FILE_DIRECTORY = os.path.abspath(os.path.join(PROJECT_PATH, "logs"))

# if file is not exist, create it.
if not os.path.exists(_LOG_FILE_DIRECTORY):
    os.mkdir(_LOG_FILE_DIRECTORY)

_LOGGER_CONFIG_PATH = os.path.join(RESOURCE_PATH, "logger_config.yml")

with open(_LOGGER_CONFIG_PATH, 'r') as f:
    log_config = yaml.load(f)
logging.config.dictConfig(log_config['logging'])

# global var
LOGGER = logging.getLogger('')

if __name__ == '__main__':
    LOGGER.info("Root logger")
