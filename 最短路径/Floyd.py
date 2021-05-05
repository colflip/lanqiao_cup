#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2021/5/5 0005 17:36
# @Author&Email: COLFLIP&colflip@163.com
# @File: Floyd.py
# @Software: PyCharm

# ---------------------------------------------
# # Foldy
#
# ---------------------------------------------

inf = 10086


def Floyd(path, graph):
    points = len(graph)
    for i in range(points):
        for j in range(points):
            if graph[i][j] != inf and graph[i][j] != 0:
                path[i][j] = i
    print(path, '\n', graph)
    for k in range(points):
        for i in range(points):
            for j in range(points):
                minG = min(graph[i][k] + graph[k][j], graph[i][j])
                if minG < graph[i][j]:
                    graph[i][j] = minG
                    path[i][j] = path[k][j]


if __name__ == "__main__":
    graph = [[0, 1, 12, inf, inf, inf],
             [inf, 0, 9, 3, inf, inf],
             [inf, inf, 0, inf, 5, inf],
             [inf, inf, 4, 0, 13, 15],
             [inf, inf, inf, inf, 0, 4],
             [inf, inf, inf, inf, inf, 0]]
    path = [[0 for i in range(len(graph))] for i in range(len(graph))]
    # graph = [[0, 1, 12, inf, inf, inf],
    #          [1, 0, 9, 3, inf, inf],
    #          [12, 9, 0, 4, 5, inf],
    #          [inf, 3, 4, 0, 13, 5],
    #          [inf, inf, 5, 13, 0, 14],
    #          [inf, inf, inf, 5, 14, 0]]
    Floyd(path, graph)
    print(path[0], '\n', graph[0])
