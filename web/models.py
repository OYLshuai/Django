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
    msg_date = models.DateTimeField(null=True, blank=True, default=None);
    msg_remark = models.CharField(max_length=255);
    deal_remark = models.CharField(max_length=255);
    deal_flag = models.CharField(max_length=2, default='0');
    deal_date = models.DateTimeField(null=True, blank=True, default=None);

    def __str__(self):
        return self.user_email

#电子商城 begin


class Employee(models.Model):
    employee_number = models.AutoField(verbose_name='员工号', primary_key=True)
    employee_name = models.CharField(max_length=30, verbose_name='姓名', editable=False)
    integration = models.IntegerField(verbose_name='持有积分', default='0')
    discount = models.FloatField(verbose_name='享有折扣', default='1')
    vip_Flag = models.BooleanField(verbose_name='会员标志', editable=False, default=False)

    def __str__(self):
        return self.employee_number


class Goods(models.Model):
    goods_number = models.AutoField(verbose_name='商品号', primary_key=True)
    goods_name = models.CharField(max_length=100, verbose_name='商品名', editable=False)
    goods_value = models.IntegerField(verbose_name='人名币价值', default='0')
    goods_integration = models.IntegerField(verbose_name='积分价值', default='0')
    goods_repertory = models.IntegerField(verbose_name='商品库存', default='0')
    day_conversion_max = models.IntegerField(verbose_name='每日兑换上限', default='0')
    goods_img = models.ImageField(verbose_name='商品图片', upload_to='img')
    goods_describe = models.CharField(max_length=1000, verbose_name='商品描述', default='null')
    goods_end_date = models.DateField(verbose_name='商品结束兑换日期', null=True, blank=True, default=None)

    def __str__(self):
        return self.goods_number


class Order(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=30, verbose_name='流水号', editable=False)
    order_remark = models.CharField(max_length=50, verbose_name='流水备注')
    order_date = models.DateField(verbose_name='兑换日期', null=True, blank=True, default=None)
    order_amount = models.IntegerField(verbose_name='兑换数量', default='1')
    order_integration = models.IntegerField(verbose_name='扣除积分', default='0')
    # 0正常  1不正常
    order_state = models.CharField(max_length=2, verbose_name='流水状态', default='0')

    def __str__(self):
        return self.order_number


    #电子商城 end