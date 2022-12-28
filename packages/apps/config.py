#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: guang
# Change Time: 2022-12-23 15:34
# File: config.py

class AppConfig:
    """
    读取应用配置
    """

    def __init__(self, app_name, app_module):
        """
        init app
        :param app_name:
        :param app_module:
        """
        # app name
        self.name = app_name
        # app module
        self.module = app_module
