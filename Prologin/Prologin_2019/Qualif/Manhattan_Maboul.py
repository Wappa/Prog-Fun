def manhattan_maboul0(m, jours, n):
    NbAmi = 0
    NbMax = 0
    Conc = []
    Sort = jours.sort()
    j=0
    mini = min(jours)
    maxi = max(jours)+1
    for i in range(mini,maxi):
        NbAmi =0
        for j in range(i,j+m,1):
            if i in jours :
                NbAmi += jours.count(i)
        Conc.append(NbAmi)
        print(Conc)

    print(min(jours))
    print(max(jours))
    print(max(Conc))


    #print(mini)
    #print(maxi)


(n, m) = list(map(int, input().split()))
jours = list(map(int, input().split()))
manhattan_maboul0(m, jours, n)
