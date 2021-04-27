#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2021/4/27 0027 10:14
# @Author&Email: COLFLIP&colflip@163.com
# @File: t21A.py
# @Software: PyCharm

# ---------------------------------------------
# # 卡片
# n记录数字使用情况，达到界值退出
# ---------------------------------------------
def get2021():
    n = [0 for i in range(10)];
    # print("n:",len(str(n)),n)
    m = 0;
    while (1):
        lenm = len(str(m));
        for i in range(0, lenm):
            x = int(str(m)[i]);
            for j in range(0, 10):
                if x == j:
                    n[x]=n[x]+1;
                    if n[x] > 2020:
                        print(x, n[x], m);
                        return ;

        m += 1;
get2021()

# ---------------------------------------------
# 方法2
# 记录数字1输出。因为1使用量最大，所以计算1使用量就是题解
# ---------------------------------------------
# ans = 0
# for i in range(10000):
#     ans += str(i).count("1")
#     if ans == 2021 or ans + str(i + 1).count("1") > 2021:
#         break
# print(i)
