#!/usr/bin/env python3
#https://youtu.be/FGC5TdIiT9U
from random import shuffle
from sys import exit

n1 = "34614"
n2 = "52876"
n3 = "72548"
nsum = "187308"

def perm(n):
    num = []
    res = ""
    for i in n:
        num.append(i)
    mid = num[1:-1]
    shuffle(mid)
    mid.insert(0, n[0])
    mid.append(n[-1])
    for i in mid:
        res += i
    return(int(res))

n_try = 0
while True:
    p1 = perm(n1)
    p2 = perm(n2)
    p3 = perm(n3) 
    psum = perm(nsum)
    
    if p1 + p2 + p3 == psum:
        print(f"Try: {n_try}")
        print(f"{p1} + {p2} + {p3} == {psum}")
        exit()
    else:
        #p123 = p1 + p2 + p3
        #print(p123, "!=", psum)
        n_try += 1
        
