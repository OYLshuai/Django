#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2018/10/11 10:48
# @Author  : 璐哥
# @File    : textdb.py

from django.http import HttpResponse

from web.models import text
from django.shortcuts import render_to_response


# 数据库操作
def testdb(request):
    ##test1 = text(id='2', name='runoob')
    ##test1.save()
    ##return HttpResponse("<p>数据添加成功！</p>")
    # 初始化
    response = ""
    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = text.objects.all()

    # 输出所有数据
    for var in list:
        response1 += var.name + " "
    response = response1
    return render_to_response('text.html',{'text': list})
    #return HttpResponse("<p>" + response + "</p>")