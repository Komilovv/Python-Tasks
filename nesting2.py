# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:09:15 2023

@author: ADMIN
"""

Buxoriy= {'full name':'Abu Abdulloh Muhammad ibn Ismoil ibn Ibrohim',
          't.yil':'810-yil',
          'v.yil':'870-yil',
          'f.asari':'Al-Jome As-Sahih',
          't.joy':'Buxoro'}
Beruniy ={'full name':'Abu Rayxon Beruniy Muhammad ibn Ahmad',
          't.yil':'973-yil',
          'v.yil':'1048',
          'f.asari':'Geodeziya',
          't.joy':'Xorazm(hozirgi Qoraqalpog`iston)'}
Qodiriy ={'full name':'Abdulla Qodiriy',
          't.yil':'1894-yil',
          'v.yil':'1938-yil',
          'f.asari':'O`tgan kunlar',
          't.joy':'Toshkent'}
Narzullayev ={'full name':'Narzullayev Anvar ',
          't.yil':'1983-yil',
          'v.yil':'hayot',
          'f.asari':'Pythonda dasturlash asoslari',
          't.joy':'Toshkent'}
info =[Buxoriy,Beruniy,Qodiriy,Narzullayev]
for shaxs in info:
    print(f"{shaxs['full name']} {shaxs['t.joy']}da tavallud topgan.")