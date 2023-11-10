# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 21:35:54 2023

@author: ADMIN
"""

good ={}
while True:
    nomi =input("Mahsulot nomini kiriting. ")
    narx = int(input(f"{nomi}ning narxini kiriting "))
    good[nomi]= narx
    if narx> 100:
        break
print(good)
    