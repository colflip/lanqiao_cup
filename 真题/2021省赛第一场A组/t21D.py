#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2021/4/27 0027 17:44
# @Author&Email: COLFLIP&colflip@163.com
# @File: t21D.py
# @Software: PyCharm




# ---------------------------------------------
# # 路径
# 局部最优
# ---------------------------------------------
# def gys(n):
#     ans = []
#     for i in range(1, int(n ** 0.5) + 1):
#         if n % i == 0:
#             ans.append(i);
#             ans.append(n // i);
#     ans = sorted(ans);
#     return ans
# def maxGys(ans1, ans2):
#     res=0;
#     for i in ans1:
#         if i in ans2:
#             if(res<i):
#                 res=i;
#     return res;
# n=2021;
# ans1=gys(n);
# min=n*n;
# out=0;
# while(n>0):
#     for i in range(n-20,n):
#         newn=i;
#         if(newn<=0):
#             newn=1;
#         ans2=gys(newn);
#         res=maxGys(ans1,ans2);
#         minn=n*newn//res;
#         if minn<min:
#             min=minn;
#     n=n-20;
#     out=min+out;
# print(out)