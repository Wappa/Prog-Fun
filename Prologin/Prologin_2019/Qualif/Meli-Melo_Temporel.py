def meli_melo_temporel0(lieux, n, etapes, v):
    Harui = 0
    Joseph = 0
    DecalageH = 0
    DecalgeJ = 0

    for Gofast in etapes:
        for i in lieux:
            if Gofast == 1 :
                DeclageH +=  




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
