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



#Prend en paramètre un graphe et renvois la liste des couples de sommets
def hopcroft(G):
    #Si le nombre de sommet est impair, inutile d'aller plus loin
    if len(G) % 2 == 0:
        return False

    #Définition des structures de donnée
    pairU = initVect(len(G), NIL)
    pairV = initVect(len(G), NIL)
    dist = initVect(len(G), INF)
    matching = 0

    #Tant qu'il y a un chemin d'augmentation
    while bfs(pairU, pairV, dist, G):
        for u in range(1, len(G)):
            #Si u est libre et qu'il y a un chemin d'augmentation depuis u
            if pairU[u] == NIL and dfs(pairV, pairU, G, dist, u):
                matching += 1

    #Renvois des résultats
    if matching == len(G) - 1:
        result = []
        for i in range(1, (int)((len(pairU) + 1) / 2)):
            result.append((i, pairU[i]))
        return result
    return False




#Renvois vrais ou faux selon s'il y a ou pas un chemin d'augmentation
def bfs(pairU, pairV, dist, G):
    Q = [] #Va contenir les sommets libres
    for u in range(1, len(pairU)):
        if pairU[u] == NIL:
            dist[u] = 0
            Q.append(u)
        else:
            dist[u] = INF
    dist[NIL] = INF

    #Tant que la queue n'est pas vide
    while len(Q) > 0:
        u = Q.pop()
        if dist[u] < dist[NIL]:
            for v in G[u]: #Pour chaque voisin de u
                if dist[pairV[v]] == INF:
                    dist[pairV[v]] = dist[u] + 1
                    Q.append(pairV[v])
    return dist[NIL] != INF




#Renvois vrais ou faux selon s'il y a ou pas un chemin d'augmentation commençant par u
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




def test(G, name):
    print("Résultat du graphe", name, ":", hopcroft(G))
    

Gsujet = [[],[7,8],[7,9],[10,11,12],[8],[7,10],[12],[1,2,5],[1,4],[2],[3,5],[3],[3,6]] #Graphe du sujet
Gfalse = [[],[7,8],[7,9],[10,11,12],[8],[7,10],[7],[1,2,5,6],[1,4],[2],[3,5],[3],[3]] #Graphe du sujet modifié pour qu'il soit faux
Gtest = [[],[2,3],[1,3,4],[1,2],[2]] #Petit graphe de test


test(Gsujet, "Gsujet")
test(Gfalse, "Gfalse")
test(Gtest, "Gtest")
