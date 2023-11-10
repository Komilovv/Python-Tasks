# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 21:19:27 2023

@author: ADMIN
"""

mahsulotlar = []
while True:
    m_nomi= input("Buyurtmangiz nomini kiriting. ")
    mahsulotlar.append(m_nomi)
    javob = input("Dasturni to'xtatish uchun 'stop' deb yozing , davom etish uchun esa 'go'  ")
    if javob == "stop":
        break
print(f"Sizning savatingizda {mahsulotlar} bor")