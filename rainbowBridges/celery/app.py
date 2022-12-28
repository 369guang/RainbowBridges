#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: guang
# Change Time: 2021/8/12 9:38 下午
from celery import Celery
from django.conf import settings


class App(Celery):
    pass


app = App('celery')
app.config_from_object('rainbowBridges.celery.config')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS, related_name="tasks")
