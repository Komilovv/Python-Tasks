# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 15:10:10 2023

@author: ADMIN
"""
def fibonachchi(x):
    """Qabul qilingan son miqdoricha fibonachchi
    ketma- ketligini chiqaruvchi funksiya"""
    sonlar=[]
    for n in range(x):
        if n==0 or n==1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[n-1]+sonlar[n-2])
    return sonlar
print(fibonachchi(10))
        

