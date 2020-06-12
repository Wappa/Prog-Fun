def manhattan_maboul0(m, jours, n):
    NbAmi = 0
    fri =0
    calend = []
    rtn = []
    a=m
    mini = min(jours)
    maxi = max(jours)+1
    i=min(jours)
    w = mini
    for i in range(0,maxi,1):
        NbAmi =0
        if i in jours:
            j = jours.count(i)
            NbAmi += j
        calend.append(NbAmi)
    print(calend)
    h=i
    for h in range (mini,maxi):
        fri = 0
        for w in range(w,a+1,1):
            if w < len(calend):
                fri += calend[w]
        rtn.append(fri)
        a += 1
        w += 1- m
    print(max(rtn))

def maxin (liste):
    mx =0
    for i in range (0,len(liste),1):
        if liste[i] > liste[i-1]:
            mx = liste[i]
    print(mx)

maxin([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3])


#(n, m) = list(map(int, input().split()))
#jours = list(map(int, input().split()))
#manhattan_maboul0(m, jours, n)
