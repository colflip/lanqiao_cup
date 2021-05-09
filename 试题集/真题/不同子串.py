#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2021/5/9 0009 8:21
# @Author&Email: COLFLIP&colflip@163.com
# @File: 不同子串.py
# @Software: PyCharm

# ---------------------------------------------
# # 
#
# ---------------------------------------------
var = '0100110001010001' # var = 'aaab' 运行结果为7 表示算法正确
num = 1 # 自身也是1个，循环中没有去考虑他串本身，所以这里基数直接设置为1
sep = 1
var_n = []
while sep < len(var):
    var_n.append(var[0:sep])
    for i in range(len(var)-sep):  # 以sep为间隔依次向前推进，sep每轮循环增1
        if var[i+1:i+sep+1] in var_n:
            continue
        else:
            var_n.append(var[i+1:i+sep+1])
    sep += 1
    num += len(var_n)
    # print(var_n)
    var_n = []
print(num)
