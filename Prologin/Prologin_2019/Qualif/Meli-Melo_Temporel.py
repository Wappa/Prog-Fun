import math

def meli_melo_temporel0(lieux, n, etapes, v):
    Harui =1
    Joseph =2
    DecalageH = 0
    DecalageJ = 0
    for i in range (0,v):
        if etapes[0] == Harui :
            for voyage in etapes[1]:
                DecalageH += lieux[etapes[1]][1]
        if etapes[0] == Joseph :
            for voyages in etapes[1]:
                DecalageJ += lieux[etapes[1]][1]

        print(etapes[1],1)







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
