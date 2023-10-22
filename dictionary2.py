# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 21:17:25 2023

@author: ADMIN
"""

info = {
        'Uzbekistan':'Tashkent',
        'Korea':'Seul',
        'UAE':'Abu Dabi',
        'UK':'London',
        'Turkey':'Anqara'}
print("Names of countries")
for key in info.keys():
    print(key.upper())
print("Capitals of the countries")
for value in info.values():
    print(value.title())