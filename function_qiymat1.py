# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 23:09:14 2023

@author: ADMIN
"""

def info_get(ism,familiya,tyil,tjoy,email):
   """Foydalanuvchidan ma'lumotlarini qabul qilib ,ularni lug`at ko'rinishda qaytaradigan funksiya"""
   contacts={'ism':ism,
             'familiya':familiya,
             'tyil':tyil,
             'tjoy':tjoy,
             'email':email
            }
   return contacts
future_leaders=[]
while True:
    print("Leader haqida ma'lumotlarni kiriting.")
    ism =input("Ismi:")
    familiya=input("Familiyasi:")
    tyil=input("Tug'ilgan yili:")
    tjoy=input("Tug'ilgan joyi:")
    email=input("Email manzili:")
    future_leaders.append(info_get(ism,familiya,tyil,tjoy,email))
    javob=input("Continue or stop ?")
    if javob=='stop':
        break
print("Leaders : ")
for leader in future_leaders:
    print(f"{leader['ism']} {leader['familiya']}, {leader['tyil']} yilda  {leader['tjoy']}da tavallud topgan. Email-addressi: {leader['email']}")
    