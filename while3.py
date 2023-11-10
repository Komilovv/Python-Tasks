# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 23:45:40 2023

@author: ADMIN
"""
topic =print("Kiritilgan sonning ildizini qaytaruvchi dastur.\n")
savol = "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    elif int(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")