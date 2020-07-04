#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    decal = []
    for i in range(d,len(a)):
        decal.append(a[i])
    for j in range(d):
        decal.append(a[j])
    for k in range(len(decal)):
        print(decal[k], end = " ")
