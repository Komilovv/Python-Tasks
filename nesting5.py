# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 21:33:46 2023

@author: ADMIN
"""

davlatlar ={'Uzbekistan':{'currency':'so`m',
                          'population':'36 million',
                          'type':'democracy only in the paper'},
            'United Kingdom':{'currency':'GBP',
                  'population':'67 million',
                  'type':'kingdom'},
            'South Korea':{'currency':'won',
                  'population':'51 million',
                  'type':'democracy'}}
davlat = input("Qaysi davlat haqida ma`lumot olishni hohlaysiz>>>").title()
if davlat in davlatlar.keys():
    info =davlatlar[davlat]
    print(f"\n{davlat}ning pul birligi {info['currency']},"
          f"\naholi soni {info['population']},"
          f"\nboshqaruv turi esa {info['type']}")
else: print("Bizda bu davlat haqida malumot yoq.")