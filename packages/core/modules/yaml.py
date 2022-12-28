#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: guang
# Change Time: 2022-12-26 18:59
# File: yaml.py
import yaml
import os

"""
app.yaml

config:
    - url:
        components: input
        values: http://www.baidu.com/
    - protocol:
        components: select
        values:
            - http
            - ws
            - ws-reverse

"""


class LoadConfig:
    """
    读取配置文件

    """

    def __init__(self, path: str):
        self.path = path

    def loading_config(self):
        """
        加载配置文件，并输出为dict
        :param path:
        :return:
        """
        if not os.path.exists(self.path):
            return {}
        with open(self.path, 'r') as fd:
            data = self.check_config(fd)
        return data

    def check_config(self, fd):
        """
        检查文件格式是否正常，并确认组件是否合法
        1.查看config是否合法
        :return:
        """
        try:
            data = yaml.load(fd, Loader=yaml.FullLoader)
            return data
        except Exception as ex:
            print("yaml文件格式错误，请检查！！！")
            # print(ex)
            exit(1)
