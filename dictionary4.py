# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 22:07:56 2023

@author: ADMIN
"""

menu = {'osh':'15','somsa':'5','manti':'13',
        'shorva':'10','makaron':'12','shashlik':'10',
        'honim':'14','mastava':'8','shovla':'12','dimlama':'15'}
print("Uchta taomni bepul tanlashingiz mumkin!")
for n in range(3):
 buyurtma=input(f"{n+1} - ")
 if buyurtma in menu:
    print(F"{buyurtma} - {menu[buyurtma]}")
 else: 
    print(f"Bizda {buyurtma}  yoq")
