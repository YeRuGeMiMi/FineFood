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
from django.http import HttpResponse
from django.utils import simplejson
from App.modules import Goods2JSON
from App.modules import Goods2String
import os
import pdb
# Create your views here.

def index(request):
	goods = Goods.objects.order_by('-created')[0:20]
	for i in range(len(goods)):
		goods[i].imguri = "uploads/"+goods[i].imguri
		
	return render_to_response('index.html',{'request':request,'goods':goods})

def loading(request):
	cs = int(request.GET.get('cs'))
	endex = 20+cs*10
	json_r = Goods.objects.order_by('-created')[20:endex]
	json_r = Goods2JSON(json_r)
	#json_r = Goods2String(json_r)
	return HttpResponse(json_r,mimetype="application/javascript") 