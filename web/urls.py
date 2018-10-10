#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2018/10/10 19:53
# @Author  : 璐哥
# @File    : urls.py

from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
]