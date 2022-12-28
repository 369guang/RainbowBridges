#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: guang
# Change Time: 2022-12-21 21:04
# File: user.py
import string
import random
from django.db import models
from packages.core.db.model import BaseModel
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator


def get_upload_to(instance, filename):
    name, ext = os.path.splitext(filename)
    random_string = ''.join(random.choices(string.ascii_letters, k=6))
    now = timezone.localtime()
    return f'user/avatar/{now.year}/{now.month}/{now.day}/{name}-{random_string}{ext}'


class User(BaseModel):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    nickname = models.CharField(_('Nick Name'), max_length=32, blank=True, null=True)
    # email = models.EmailField(_('email address'), blank=True, null=True)

    avatar = models.ImageField(_('头像'), null=True, blank=True,
                               upload_to=get_upload_to)
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
