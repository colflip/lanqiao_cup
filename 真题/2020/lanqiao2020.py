# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2021/3/4 0004 22:43
# @Author&Email: COLFLIP&colflip@163.com
# @File: lanqiao2020.py
# @Software: PyCharm

# ---------------------------------------------
# 平面切分
# 两条直线相交方程
# set（） list
# ---------------------------------------------
# n = int(input());
# lines = [];
# for i in range(n):
#     a, b = list(map(int, input().split()))
#     lines.append((a, b))
# lines = list(set(lines))
#
#
# def getNode(line1, line2):
#     A1 = line1[0]
#     B1 = line1[1]
#     A2 = line2[0]
#     B2 = line2[1]
#     if A1 - A2 == 0:
#         return
#     x = (B2 - B1) / (A1 - A2)
#     y = A1 * x + B1
#     x = round(x, 10)
#     y = round(y, 10)
#     print(x, y)
#     return (x, y)
#
#
# ci = [1] * (n + 1)
# node = set()
# for i in range(0, n):
#     node.clear()
#     for j in range(i):
#         res = getNode(lines[i], lines[j])
#         if res == None: continue
#         node.add(res)
#     ci[i] += len(node)
# print(sum(ci[:n]) + 1)
# print(ci)

# ---------------------------------------------
# # 明明的排序
# 一行多值输入list = map（） 字符串str
# ---------------------------------------------
# n = int(input())
# List = list(map(int, input().split()))
# List = list(set(List))
# List.sort()
# res = str(List[0])
# for i in range(1, len(List)):
#     res += " " + str(List[i])
# print(len(List))
# print(res)

# ------------------------------------------------------------------------------------------
# # 装饰珠
# 多行输入
# DP
# https: // www.lanqiao.cn / problems / 507 / learning /
# ---------------------------------------------
# import numpy as np
#
# n = np.zeros(6)
# nLevel = np.zeros(4)
# for i in range(6):
#     List = list(map(int, input().split()))
#     n[i] = List[0]
#     for j in range(1, len(List)):
#         nLevel[List[j] - 1] = nLevel[List[j] - 1] + 1
# m = int(input())
# md = np.zeros([m, 2])
# mw = np.zeros([5, 10])
# for i in range(m):
#     List = list(map(int, input().split()))
#     md[i, 0] = List[0]
#     md[i, 1] = List[1]
#     le = int(md[i, 0])
#     for j in range(1, len(List) - 1):
#         if int(List[j + 1]) > int(mw[le, j]):
#             mw[le, j] = List[j + 1]
#         if (j + 1) > md[i, 1] and md[i, 1] < 8:
#             for k in range(j + 1, 8):
#                 mw[le, k] = mw[le, k - 1]
# print(mw)
# res = 0
# for i in range(0, int(nLevel[3]) + 1):
#     print("3")
#     for j in range(0, int(nLevel[2]) - i + 1):
#         print("2")
#         for k in range(0, int(nLevel[1]) - i - j + 1):
#             print("1")
#             for l in range(0, int(nLevel[0]) - i - j - k + 1):
#                 a = 0
#                 b = 0
#                 c = 0
#                 d = 0
#                 if (i > 7):
#                     a = 7;
#                 else:
#                     a = i;
#                 if (j > 7):
#                     b = 7;
#                 else:
#                     b = j;
#                 if (k > 7):
#                     c = 7;
#                 else:
#                     c = k;
#                 if (l > 7):
#                     d = 7;
#                 else:
#                     d = l;
#                 res = max(res, mw[4][a] + mw[3][b] + mw[2][c] + mw[1][d]);
#                 print("rse", res)
# print(res)
# # print(n, nLevel, m, md)

# ---------------------------------------------
# # 数字三角形
# DP
# ---------------------------------------------
# import numpy as np
#
# n = int(input())
# m = np.zeros([n, n])
# for i in range(n):
#     List = list(map(int, input().split()))
#     lLen = len(List)
#     for j in range(lLen):
#         m[i, j] = List[j]
# dp = np.zeros([n + 1, n + 1])
# dp[1][1] = m[0][0]
# for i in range(2, n + 1):
#     for j in range(1, i + 1):
#         dp[i][j] = m[i - 1][j - 1] + max(dp[i - 1][j - 1], dp[i - 1][j])
# print((max(dp[n][int((n + 1) / 2)], dp[n][int((n + 2) / 2)])))

# ---------------------------------------------
# # 单词分析
# set,count,sort,取值输出
# ---------------------------------------------
# import numpy as np
#
# word = str(input())
# wordN = str(set(word))
# n, r2 = [], 0
# for i in range(len(wordN)):
#     m = word.count(wordN[i])
#     n.append((wordN[i], m))
# n.sort(reverse=True)
# for x in n:
#     if x[1] > r2:
#         r2 = x[1]
#         r1 = x[0]
# print(r1)
# print(r2)

# ---------------------------------------------
# # 成绩统计
# round(x[, n])
# ---------------------------------------------
# n = int(input())
# j, k = 0, 0
# for i in range(n):
#     m = int(input())
#     if m >= 60:
#         j += 1
#     if m >= 85:
#         k += 1
# print(str(round(j / n * 100)) + "%")
# print(str(round(k / n * 100)) + "%")

# ---------------------------------------------
# # 排序
# ---------------------------------------------
# 首先要注意最后得到的字符串全是英文小写字母并且不重复。接下来进行分析，最后要求结果在最短的前提下字典序最小。那么我们先想办法找到最短的结果。
# 最短，那是能多短就多短。最短是长度是1，但是肯定不可能，因为他还要求字符串进行了100次交换，那么长度为2可不可以呢？也不行，长度为2的字符串最多进行一次交换。
# 一个长度为n的字符串，如果进行冒泡排序，假设他每次比较都进行了交换，那么它最多交换 (n-1)+(n-2)+…+1 = n*(n-1）/2 （进行n-1趟操作，第一趟操作交换n-1次，之后每趟交换的次数依次递减）。
# 在n*(n-1）/2>=100的前提下，n的最小值是15。也就是说，最后结果的字符串的长度至少15（低于15,它根本连交换100次的要求都达不到）。接下来再和题目要求的字典序最小一起考虑。
# 首先了解一下字典序：字典序是指从前到后比较两个字符串的大小的方法。首先比较第一个字符，如果不同则第一个字符较小的字符串更小，如果相同则继续比较第2个字符…如此继续，来比较整个字符串的大小。
# 现在我们知道字符串全是英文小写字母，并且长度为15且各不相同，那么我们可以确定这15个字母就是前15个小写英文字母abcdefghijklklmno，怎么排现在还不知道。
# 用逆向思维思考，若这15个字母每次冒泡两两比较都进行交换，能交换 15*(15-1) = 105次，那这个字符串只可能是这15个字母的逆序：onmlkjighfedecba。
# 然后我们再想办法减少逆序字符串的5次比较，并且使最后得到的结果字典序最小，只需要把逆序字符串的第六位提前至第一位：jonmlkighfedecba。
# 在这种情况下，字典序就是最小的，我只需要第一位比你小，我就是字典序最小的。而且第1，2，3，4，5趟，每次j会分别和o,n,m,k,l进行比较，但是不交换，这样就省下了5次交换，且最后一共交换105-5=100次。

# ---------------------------------------------
# # 跑步锻炼
#   datetime,weekday(),day()
# ---------------------------------------------
# from datetime import *
# start,end=date(2000,1,1),date(2020,10,2)
# tmp=timedelta(days=1)
# ans=0
# while start!=end:
#     if start.weekday()==0 or start.day==1:
#         ans+=2
#     else:
#         ans+=1
#     start+=tmp
# print(ans)

# ---------------------------------------------
# # 寻找2020
# ---------------------------------------------
# nums,result=[],0
# with open("2020.txt") as fp:
#     for a in fp.readlines():
#         nums.append(list(a.strip()))
# move=[[0,1],[1,0],[1,1]]
# for y in range(len(nums)):
#     for x in range(len(nums[0])):
#         for yy,xx in move:
#             num=str(nums[y][x])
#             for m in range(1,4):
#                 y_,x_=y+(yy*m),x+(xx*m)
#                 if 0<=y_<len(nums) and 0<=x_<len(nums[0]):
#                     num+=str(nums[y_][x_])
#                 else:
#                     break
#             if num=='2020':
#                 result+=1
# print(result)

# ---------------------------------------------
# # 画图
# ---------------------------------------------
# import numpy as np
# import matplotlib.pyplot as plt
# y=np.random.standard_exponential(10)
# x=range(len(y))
# plt.plot(x,y,"r")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()

# ------------------------------------------------------------------------------------------
# # 郊外种树
# https://blog.csdn.net/weixin_39533361/article/details/112331096
# ---------------------------------------------

import numpy as np
n = int(input())
arr = np.zeros([n, 3], dtype=np.int)  # arr = [x,y,h]
dis = np.zeros([n, n])
minn = np.full(n, np.power(10, 7), dtype=np.float)
vis = np.zeros(n)

for x in range(n):
    arr[x] = [int(_) for _ in input().split()]

# 初始化距离
for i in range(n):
    for j in range(i + 1, n):
        dis[i][j] = dis[j][i] = np.sqrt(
            np.square(arr[i][0] - arr[j][0]) + np.square(arr[i][1] - arr[j][1])) + np.square(arr[i][2] - arr[j][2])

minn[0] = 0
for i in range(n):
    tmp = -1
    for j in range(n):
        if vis[j] == False:
            if tmp == -1 or minn[j] < minn[tmp]: tmp = j
    vis[tmp] = True
    for j in range(n):
        if vis[j] == False:
            minn[j] = minn[j] if (minn[j] < dis[tmp][j]) else dis[tmp][j]
re = 0.0
for i in range(1, n): re += minn[i]
print('%.2f' % re)


