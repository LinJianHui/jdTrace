# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Product(models.Model):
    """docstring for ClassName"""

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['orderNum']

    name = models.CharField(max_length=256)
    shopId = models.CharField(null=True, max_length=256)
    url = models.CharField(max_length=256)
    imgUrl = models.CharField(max_length=256)
    orderNum = models.CharField(max_length=256)
    updateTime = models.DateTimeField()


class Price(models.Model):
    """docstring for Price"""

    def __str__(self):
        return self.price

    product = models.ForeignKey('shop.Product', verbose_name='对应的商品')
    price = models.FloatField()
    date = models.DateField()
