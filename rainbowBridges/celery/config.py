#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: guang
# Change Time: 2021/8/12 9:38 下午
from django.conf import settings
from celery import platforms
from celery.schedules import crontab

BROKER_URL = settings.CELERY_BROKER_URL
CELERY_RESULT_BACKEND = settings.CELERY_RESULT_BACKEND
CELERY_TIMEZONE = settings.TIME_ZONE
CELERY_TASK_SERIALIZER = 'pickle'
CELERY_RESULT_SERIALIZER = 'pickle'
CELERY_ACCEPT_CONTENT = ['pickle', 'json']

platforms.C_FORCE_ROOT = True

CELERYBEAT_SCHEDULE = {
    # 'sync_department': {
    #     'task': 'apps.user.tasks.get_department_staff',
    #     'schedule': crontab(minute='01', hour='*/12')
    # },

}

CELERY_ROUTES = {
    'apps.*': 'common',
}
