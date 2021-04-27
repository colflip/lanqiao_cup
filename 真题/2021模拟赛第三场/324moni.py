#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2021/4/18 0018 22:17
# @Author&Email: COLFLIP&colflip@163.com
# @File: 324moni.py
# @Software: PyCharm


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    while a % b != 0:
        temp = b;
        b = a % b;
        a = temp;
    return b


cnt = 0
for i in range(1, 2021):
    if gcd(i, 2020) == 1:
        cnt += 1;
print(cnt)