#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-06-25 14:54:34
# @Author  : yfl (yerugemimi@gmail.com)
# @Link    : https://github.com/YeRuGeMiMi
# @Version : $Id$
from django.shortcuts import render
from django.shortcuts import render_to_response
from FineFood import conf
from App.models import Goods
import os
# Create your views here.

def index(request):
	goods = Goods.objects.all()
	for i in range(len(goods)):
		goods[i].imguri = "uploads"+os.path.sep+goods[i].imguri
		

	return render_to_response('index.html',{'request':request,'goods':goods})