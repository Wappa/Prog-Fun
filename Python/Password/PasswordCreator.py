import random
import string
from random import randrange

def mdp():
    mdp = ""
    i = 0
    NbL = 0
    NbN = 0
    longu = input("Password Length \n")
    long = int(longu)
    if long <= 6:
        raise Exception("Password too short ")
    NbLettre = input("Give us the number of letter for the password \n")
    NbChiffre = input("Give us the number of number for the password \n")
    NbSpeciaux = long -(int(NbLettre)+int(NbChiffre))
    if int(NbLettre) + int(NbChiffre)  + NbSpeciaux != long:
        raise Exception("Sum of Number and Letter must be equal to Length \n")
    while i < long:
        Rnd = random.randrange(0,2,1)
        if (Rnd == 0 and NbL < int(NbLettre)):
            mdp += random.choice(string.ascii_letters)
            NbL +=1
        elif(Rnd == 1 and NbN < int(NbChiffre)):
            mdp+= str(random.randrange(10))
            NbN +=1
        else:
            mdp+= random.choice(string.punctuation)
        i+=1
    return mdp

print(mdp())
