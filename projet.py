# -*- coding: utf-8 -*-

global INF
global NIL

INF = 999999999
NIL = 0

def initVect(n,a):
    V=[]
    for j in range(n):
        V.append(a)
    return V

def hopcroft(G):
    pairU = initVect(len(G), NIL)
    pairV = initVect(len(G), NIL)
    dist = initVect(len(G), INF)
    matching = 0
    while bfs(pairU, pairV, dist, G):
        for u in range(1, len(G)):
            if pairU[u] == NIL and dfs(pairV, pairU, G, dist, u):
                matching += 1
    if matching == len(G) - 1:
        result = []
        for i in range(1, (int)((len(pairU) + 1) / 2)):
            result.append((i, pairU[i]))
        return result
    return False


def bfs(pairU, pairV, dist, G):
    Q = []
    for u in range(1, len(pairU)):
        if pairU[u] == NIL:
            dist[u] = 0
            Q.append(u)
        else:
            dist[u] = INF
    dist[NIL] = INF
    while len(Q) > 0:
        u = Q.pop()
        if dist[u] < dist[NIL]:
            for v in G[u]:
                if dist[pairV[v]] == INF:
                    dist[pairV[v]] = dist[u] + 1
                    Q.append(pairV[v])
    return dist[NIL] != INF


def dfs(pairV, pairU, G, dist, u):
    if u != NIL:
        for v in G[u]:
            if dist[pairV[v]] == dist[u] + 1:
                if dfs(pairV, pairU, G, dist, pairV[v]):
                    pairV[v] = u
                    pairU[u] = v
                    return True
        dist[u] = INF
        return False
    return True


Gsujet = [[],[7,8],[7,9],[10,11,12],[8],[7,10],[12],[1,2,5],[1,4],[2],[3,5],[3],[3,6]]
Gfalse = [[],[7,8],[7,9],[10,11,12],[8],[7,10],[7],[1,2,5,6],[1,4],[2],[3,5],[3],[3]]
Gtest = [[],[2,3],[1,3,4],[1,2],[2]]


print(hopcroft(Gsujet))
print(hopcroft(Gtest))
print(hopcroft(Gfalse))










