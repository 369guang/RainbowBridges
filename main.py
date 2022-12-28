#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: guang
# Change Time: 2022-12-15 19:37
# File: main.py
from packages.core.modules import loading


def main():
    apps = loading.Config("dingtalkbot")
    apps.start()


main()
