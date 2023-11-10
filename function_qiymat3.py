# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 23:58:16 2023

@author: ADMIN
"""
def tubson(a,b):
    tub=[]
    for x in range(a,b+1):
        tu=True
        if x==1:
            tu=False
        elif x==2:
            tu=True
        else:
            for n in range(2,x):
                if x%n==0:
                    tu=False
        if tu:
            tub.append(x)
    return tub
son=tubson(23,6454)
print(son)
