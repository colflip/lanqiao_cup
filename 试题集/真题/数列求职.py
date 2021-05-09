#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2021/5/9 0009 8:27
# @Author&Email: COLFLIP&colflip@163.com
# @File: 数列求职.py
# @Software: PyCharm

# ---------------------------------------------
# # 
#
# ---------------------------------------------
arr = [0 for _ in range(20190325)]

arr[0] = arr[1] = arr[2] = 1

for i in range(3, 20190324):

    arr[i] = (arr[i - 1] + arr[i - 2] + arr[i - 3])

print(arr[20190323])
