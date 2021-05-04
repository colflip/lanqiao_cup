#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2021/4/27 0027 17:44
# @Author&Email: COLFLIP&colflip@163.com
# @File: t21D.py
# @Software: PyCharm

import time

start = time.time()


def gys(a, b):
    while (b != 0):
        temp = a % b
        a = b
        b = temp
    print("a", a)
    return a


def gbs(a, b):
    res = a * b / gys(a, b)
    return res


def minDp(i, j):
    mindp = 999999999999
    for m in range(i - buzhang, i):
        for n in range(j - buzhang, j):
            if mindp > dp[m][n]:
                mindp = dp[m][n]
    return mindp


buzhang = 21
dp = [[9999999] * (2021 + buzhang) for i in range(2021 + buzhang)]
map1 = [[0] * (2021) for i in range(2021)]
for i in range(0, 2021):
    for j in range(i, 2021):
        if i == j:
            map1[i][j] = 0
        else:
            map1[i][j] = gbs(i + 1, j + 1)
            map1[j][i] = map1[i][j]
print(map1)
for i in range(buzhang, 2021 + buzhang):
    for j in range(buzhang, 2021 + buzhang):
        if i == buzhang and j == buzhang:
            dp[i][j] = map1[i - buzhang][j - buzhang]
        else:
            dp[i][j] = map1[i - buzhang][j - buzhang] + minDp(i, j)
print(dp[-1][-1])
end = time.time()

print('Running time: %s Seconds' % (end - start))


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
