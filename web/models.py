# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models

# Create your models here.

class text(models.Model):
     id = models.BigIntegerField
     name = models.CharField(max_length=20, default='a')
     age = models.IntegerField(null=True)

class Book(models.Model):
    book_name = models.CharField(max_length=64)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.book_name

class User(models.Model):
    user_name = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    user_email = models.EmailField()
    user_phone = models.CharField(max_length=18, default=' ')

    def __unicode__(self):
        return self.user_name

class Message(models.Model):
    user_email = models.EmailField();
    message = models.CharField(max_length=255);
    msg_date = models.DateTimeField();
    msg_remark = models.CharField(max_length=255);
    deal_remark = models.CharField(max_length=255);
    deal_flag = models.CharField(max_length=2, default='0');
    deal_date = models.DateTimeField();

    def __unicode__(self):
        return self.user_email