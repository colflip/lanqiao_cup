#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2021/5/7 0007 10:54
# @Author&Email: COLFLIP&colflip@163.com
# @File: 进制转换.py
# @Software: PyCharm

# ---------------------------------------------
# # 进制转换
#
# ---------------------------------------------
# 16->8
# n=input()
# a=int(n,16)
# b=format(a,'o')
# print(b)

# 16->10
# n=input()
# a=int(n,16)
# print(a)

# 10->16
# n=int(input())
# a=format(n,'X')
# print(a)

# 10->8
n = int(input())
a = format(n, 'o')
print(a)
