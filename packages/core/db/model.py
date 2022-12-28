#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: guang
# Change Time: 2022-12-24 17:03
# File: model.py
from django.db import models
from django.db.models.query import QuerySet


class SoftDeletableQuerySetMixin(object):
    """
    软删除基类
    """

    def delete(self):
        """
        标记删除
        :return:
        """
        self.update(is_deleted=True)


class SoftDeletableQuerySet(SoftDeletableQuerySetMixin, QuerySet):
    pass


class SoftDeletableManagerMixin(object):
    """
    模型管理模块
    """
    _queryset_class = SoftDeletableQuerySet

    def get_queryset(self):
        """
        处理查询
        :return:
        """
        kwargs = {'model': self.model, 'using': self._db}
        if hasattr(self, '_hints'):
            kwargs['hints'] = self._hints

        return self._queryset_class(**kwargs).filter(is_deleted=False)


class SoftDeletableManager(SoftDeletableManagerMixin, models.Manager):
    pass


class BaseModel(models.Model):
    """
    带软删除的基础模型
    """
    is_deleted = models.BooleanField(default=False)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        abstract = True

    objects = SoftDeletableManager()

    def delete(self, using=None, soft=True, *args, **kwargs):
        """
        删除
        :param using:
        :param soft:
        :param args:
        :param kwargs:
        :return:
        """
        if soft:
            self.is_deleted = True
            self.save(using=using)
        else:
            return super(BaseModel, self).delete(using=using, *args, **kwargs)
