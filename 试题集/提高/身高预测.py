#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2021/5/7 0007 11:34
# @Author&Email: COLFLIP&colflip@163.com
# @File: 身高预测.py
# @Software: PyCharm

# ---------------------------------------------
# # 身高预测
#
# ---------------------------------------------
list=list(map(float,input().split()))
if list[0]==1:
    height=(list[1]+list[2])/2*1.08
else:
    height=(list[1]+list[2])/2
print(height)