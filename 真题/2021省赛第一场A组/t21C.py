
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2021/4/27 0027 17:20
# @Author&Email: COLFLIP&colflip@163.com
# @File: t21C.py
# @Software: PyCharm

# ---------------------------------------------
# # 货物摆放
#  因式分解
# ---------------------------------------------

n=2021041820210418
ans=[]
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        ans.append(i)
        ans.append(n//i)
res=set()
for i in ans:
    for j in ans:
        for k in ans:
            if i*j*k==n:
                res.add((i,j,k))
print(len(res),res)
