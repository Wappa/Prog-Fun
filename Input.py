#!/usr/bin/env python
# coding: utf-8
 
# In[9]:
 
 
'''
Welcome to world of Competitve Programming!
'''
# Taking Integer as an input
n = int(input())
print(n)
 
-----------------------------------
 
 
# Taking string as an input
s = input() # This input format is valid for python 3
print(s)
 
 
-----------------------------------
 
 
'''
a b c
1 2 3
'''
a,b,c = map(int,input().split())
print(a+b+c)
 
 
---------------------------------------------------------------------
 
 
'''
a b c d
1 2 3 4
'''
all = [int(i) for i in input().split()] # List comprehension
sum=0
for i in all:
    sum += i
print(sum)
 
 
-------------------------------------------------------------------------
 
 
'''
5
1 1 0 0 2
'''
n = int(input()) #5
all = [int(i) for i in input().split()]
print(all)
 
 
 
---------------------------------------------------------------------------
 
'''
3
1
2
3
'''
n = int(input())
for i in range(n):
    tc = int(input())
 
 
---------------------------------------------------------------------------------
 
 
'''
2
3
1 2 3
4
1 2 3 4
'''
q = int(input()) # Number of quiries
for i in range(q):
    n = int(input()) # Input size
    all = [int(i) for i in input().split()] # Elements of the list or array.
 
 
-----------------------------------------------------------------------------------------
 
 
'''
4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
'''
n = int(input())
for i in range(n):
    all = [int(i) for i in input().split()]
 
 
----------------------------------------------------------------------------------------
 
 
 
a=[1,2,3,4,5]
for i in a:
    print(i) #Elements are printed in new line
 
------------------------------------------------------------
 
 
a=[1,2,3,4,5]
for i in a:
    print(i,end=' ') #Elements are printed in the same line
 
 
---------------------------------------------------------------------------------
 
 
a=[1,2,3,4,5]
for i in range(0,5):
    print(a[i])
 
 
---------------------------------------
 
 
for i in range(1,11,2):
    print(i)
 
 
-----------------------------
