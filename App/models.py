#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-06-25 14:18:39
# @Author  : yfl (yerugemimi@gmail.com)
# @Link    : https://github.com/YeRuGeMiMi
# @Version : $Id$
from django.db import models

# Create your models here.
class Goods(models.Model):
	'''
	商品信息
	'''

	goodsname = models.CharField(max_length=255,db_column='goodsname')
	goodstitle = models.CharField(max_length=255,db_column='goodstitle')
	imguri = models.CharField(max_length=255,db_column='imguri')
	created = models.IntegerField(db_column='created')
	status = models.IntegerField(db_column='status')
	gtype = models.IntegerField(db_column='type')
	intro = models.CharField(max_length=255,db_column='intro')

	class Meta(object):
		db_table = 'goods'
		
			