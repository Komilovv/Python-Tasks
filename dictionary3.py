# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 21:36:47 2023

@author: ADMIN
"""

info = {
        'Uzbekistan':'Tashkent',
        'Korea':'Seul',
        'UAE':'Abu Dabi',
        'UK':'London',
        'Turkey':'Anqara'}
davlat = input("Yoqtirgan davlatingizni nomini kiriting>>>")
if davlat in info:
    print(f"{davlat}ning poytaxti {info[davlat]}")
else:
    print("Bizda bunday malumot yo'q")