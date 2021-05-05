# https://zhuanlan.zhihu.com/p/63395403
def Dijkstra(start: int, graph: list):
    s = [start]
    t = [x for x in range(len(graph)) if x != start]
    dis = graph[start]
    while len(t):
        print("---", s, t, dis)
        idx = t[0]
        for i in t:
            if dis[i] < dis[idx]:
                idx = i

        t.remove(idx)
        s.append(idx)

        for i in t:
            if dis[idx] + graph[idx][i] < dis[i]:
                dis[i] = dis[idx] + graph[idx][i]

    return dis

if __name__ == "__main__":
    inf = 10086
    graph = [[0, 1, 12, inf, inf, inf],
             [inf, 0, 9, 3, inf, inf],
             [inf, inf, 0, inf, 5, inf],
             [inf, inf, 4, 0, 13, 15],
             [inf, inf, inf, inf, 0, 4],
             [inf, inf, inf, inf, inf, 0]]
    # graph = [[0, 1, 12, inf, inf, inf],
    #          [1, 0, 9, 3, inf, inf],
    #          [12, 9, 0, 4, 5, inf],
    #          [inf, 3, 4, 0, 13, 5],
    #          [inf, inf, 5, 13, 0, 14],
    #          [inf, inf, inf, 5, 14, 0]]
    dis = Dijkstra(0, graph)
    print(dis)

