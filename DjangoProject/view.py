#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2018/10/10 19:44
# @Author  : 璐哥
# @File    : view.py

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def hello(request):
    context = {}
    context['hello'] = 'Hello ssss!'
    return render(request, 'dello.html', context)