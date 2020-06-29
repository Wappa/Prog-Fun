import math

def meli_melo_temporel0(lieux, n, etapes, v):
    Harui =1
    Joseph =2
    DecalageH = 0
    DecalageJ = 0
    for i in range (0,v):
        if etapes[i]["voyageur"] == Harui :
            for j in range (0,n):
                if etapes[i]["destination"] == lieux[j]["id"]:
                    DecalageH = lieux[j]["decalage"]
        if etapes[i]["voyageur"] == Joseph :
            for j in range (0,n):
                if etapes[i]["destination"] == lieux[j]["id"]:
                    DecalageJ = lieux[j]["decalage"]
        if (DecalageH < 0 and DecalageJ < 0) or (DecalageH > 0 and DecalageJ > 0):
            print(abs(DecalageH - DecalageJ))
        if (DecalageH <= 0 and DecalageJ >= 0) or (DecalageH >= 0 and DecalageJ <= 0):
            print(abs(DecalageH)+abs(DecalageJ))




n = int(input())
liste_p = [None] * n
for i in range(0, n):
    (id, decalage) = list(map(int, input().split()))
    lieux_i = {"id":id, "decalage":decalage}
    liste_p[i] = lieux_i
v = int(input())
liste_e = [None] * v
for j in range(0, v):
    (voyageur, destination) = list(map(int, input().split()))
    etape_i = {"voyageur":voyageur, "destination":destination}
    liste_e[j] = etape_i
meli_melo_temporel0(liste_p, n, liste_e, v)
