#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2018/10/10 19:53
# @Author  : 璐哥
# @File    : urls.py

from django.conf.urls import url
from . import views
from . import textdb


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^testdb$', textdb.testdb),
    url(r'^add_book$', views.add_book, ),
    url(r'^show_books$', views.show_books, ),
    url(r'^del_book$', views.del_book, ),
    url(r'^check_user$', views.check_user, ),
    url(r'^show_message$', views.show_message, ),
    url(r'^mod_msg$', views.mod_msg, ),
    url(r'^add_msg$', views.add_msg, ),
    url(r'^get_users$', views.get_users, ),
]