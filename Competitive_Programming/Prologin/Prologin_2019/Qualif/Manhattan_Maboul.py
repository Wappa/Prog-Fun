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
    if mini == maxi-1:
        rtn.append(jours.count(mini))
        print(max(rtn))
    else :
        for i in range(0,maxi,1):
            NbAmi =0
            if i in jours:
                j = jours.count(i)
                NbAmi += j
            calend.append(NbAmi)
        if m == 1:
            for m in range (mini,maxi-1):
                if calend[m] != 0 and calend [m+1] != 0:
                    print(calend[m]+calend[m+1])
        else:
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


(n, m) = list(map(int, input().split()))
jours = list(map(int, input().split()))
manhattan_maboul0(m, jours, n)
