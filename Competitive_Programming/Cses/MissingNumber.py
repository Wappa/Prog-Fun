def MissingNumber(m):
    a = m.sort()
    for i in range(a):
        if a[i+1] != a[i] +1:
            print(a[i] +1)



n = int(input())
m = [int(i) for i in input().split()]
MissingNumber(m)
