#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: guang
# Change Time: 2022-12-26 18:49
# File: loading.py

# 实现功能，扫描模块，相对路径为 project/plugins
# 启动方法为start
#

import os
from .yaml import LoadConfig


class Config:
    def __init__(self, app_name):
        root_path = os.path.dirname(os.path.realpath('__file__'))
        self.app_name = app_name
        self.module_path = f"{root_path}/plugins/{self.app_name}"
        self.config()

    def start(self):
        """
        启动函数
        :return:
        """
        pass

    def config(self):
        """
        配置项，可以有lable+(Input输入框, Select选择器, Radio单选框, Switch开关)
        :return:
        """
        load_config = LoadConfig(f'{self.module_path}/app.yaml')
        data = load_config.loading_config()
        config = data.get('config')
        for item in config:
            print(item)

    def components(self, data):
        """
        组件化，构建class
        :param data:
        :return:
        """
        pass

