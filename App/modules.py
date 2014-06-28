#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-06-25 14:54:34
# @Author  : yfl (yerugemimi@gmail.com)
# @Link    : https://github.com/YeRuGeMiMi
# @Version : $Id$

import json

#将Goods对象数组转换为json
def Goods2JSON(goods):
	goods_j = []
	for good in goods:
		goods_j.append( {
		'goodstitle':good.goodstitle,
		'imguri':good.imguri,
		'intro':good.intro})

	return json.dumps(goods_j)

#将Goods对象数组转换为json 字符串
def Goods2String(goods):
	goods_j = ["["]
	for good in goods:
		m = "{goodstitle:"+good.goodstitle+",imguri:"+good.imguri+",intro:"+good.intro+"}"
		goods_j.append(m)

	goods_j.append("]")

	return "".join(goods_j)