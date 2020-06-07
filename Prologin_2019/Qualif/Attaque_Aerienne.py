def arnaque_aerienne0(prix_initial, billets, n):
    arnaque = 0
    for i in range(n):
        if(prix_initial > billets[i]):
            arnaque +=1
    if (arnaque < 3):
        print("Ok bon voyage, bisous, n'oublie pas de m'envoyer des photos !")
    else:
        print("ARNAQUE !")

prix_initial = int(input())
n = int(input())
billets = list(map(int, input().split()))
arnaque_aerienne0(prix_initial, billets, n)
