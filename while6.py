# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 21:56:15 2023

@author: ADMIN
"""

e_mart = {'kampot': 20, "go'sht": 90, 'pista': 150,
          'cake':200}
royxat = ['pista', 'cake', 'shaftoli', 'shashlik','kampot']
while  royxat :
    fav =royxat.pop()
    if fav in e_mart:
        print(f"{fav}ning narxi {e_mart[fav]} ming so`m ")
    else:
        print(f"Bizda {fav} mahsuloti yo`q")