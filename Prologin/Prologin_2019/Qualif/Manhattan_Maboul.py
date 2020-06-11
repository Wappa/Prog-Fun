def manhattan_maboul0(m, jours, n):
    NbAmi = 0
    fri =0
    calend = []
    rtn = []
    w =0
    mini = min(jours)
    maxi = max(jours)+1
    i=min(jours)
    for i in range(i,maxi,1):
        NbAmi =0
        if i in jours:
            j = jours.count(i)
            NbAmi += j
        #print(NbAmi)
        calend.append(NbAmi)
    print(calend)

(n, m) = list(map(int, input().split()))
jours = list(map(int, input().split()))
manhattan_maboul0(m, jours, n)
