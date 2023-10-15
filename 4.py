# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:43:56 2023

@author: ADMIN
"""
soz = {'refuse':'inkor qilmoq','get this':'qara, etibor ber'}
user = soz.get(input("So`z kiritaolasizmi ?  "))
if user !=None:
    print(user)
else:
    print("Bunday so`z mavjud emas")