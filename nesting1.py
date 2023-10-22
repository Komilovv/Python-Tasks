# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 17:43:55 2023

@author: ADMIN
"""

Buxoriy= {'full name':'Abu Abdulloh Muhammad ibn Ismoil ibn Ibrohim',
          't.yil':'810-yil',
          'v.yil':'870-yil',
          'f.asari':'Al-Jome As-Sahih'}
Beruniy ={'full name':'Abu Rayxon Beruniy Muhammad ibn Ahmad',
          't.yil':'973-yil',
          'v.yil':'1048',
          'f.asari':'Geodeziya'}
Qodiriy ={'full name':'Abdulla Qodiriy',
          't.yil':'1894-yil',
          'v.yil':'1938-yil',
          'f.asari':'O`tgan kunlar'}
Narzullayev ={'full name':'Narzullayev Anvar ',
          't.yil':'1983-yil',
          'v.yil':'hayot',
          'f.asari':'Python'}
info =[Buxoriy,Beruniy,Qodiriy,Narzullayev]
for person in info:
    if person['v.yil']!='hayot':
      print(f"{person['full name']} {person['t.yil']}da tavallud topgan,{person['v.yil']}da vafot etgan .\nMashhur asari {person['f.asari']}. ")
    else:
        print(f"{person['full name']} {person['t.yil']}da tavallud topgan, u  kishi {person['v.yil']} , hali ko'p ishlar qilishi kerak.\nMashhur asari {person['f.asari']}. ")




