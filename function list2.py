# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 12:25:04 2023

@author: ADMIN
"""
def bahola(ismlar):
    baholar={}
    for ism in ismlar:
        baho=input(f"{ism}ning bahosini kiriting.")
        baholar[ism]=baho
    return baholar

talabalar=['Ali','Akbar','Ahad']
baholar=bahola(talabalar[:])
print(baholar)
