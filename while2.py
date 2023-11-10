# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 22:31:37 2023

@author: ADMIN
"""

while True:
    savol = input("Yoshingizni kiriting?\nDasturni to'xtatish uchun 'exit' or 'quit' deb yozing.")
    if savol == 'exit' or savol=='quit':
        break
    yosh = int(savol)
    if yosh <=7 or yosh >=65:
        narx = 0
    elif 7 < yosh <= 18:
        narx =5000
    else: 
        narx=10000
        
    if narx ==0:
        print("Siz uchun kirish bepul.")
    else: 
        print(f"Biletning narxi atiga {narx} so`m. ")
print("E'tiboringiz uchun rahmat !!!")