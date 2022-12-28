#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: guang
# Change Time: 2022-12-21 21:21
# File: util.py
import os


def check_path(path: str) -> bool:
    """
    检查文件或者目录是否存在
    :param path: 路径
    :return:
    """

    return os.path.exists(path)
