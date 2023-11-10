# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 15:46:49 2023

@author: ADMIN
"""
# Funksiya 4-task.
#def katta_son(a,b):
 #   """Foydalanuvchidan ikkita son olib ularning kattasini kosolga chiqaradigan,agar sonlar teng bo`lsa  tengligi haqida habar beradigan funksiya"""
  #  if a<b:
   #     print(f"{b} katta {a} dan.")
        
    #elif a>b:
   #     print(f"{a} katta {b} dan.")
    #else: 
     #   print("Sonlar teng.")
#katta_son(97457,567457)
#katta_son(-135,0.1)
#katta_son(98,98)

# Funksiya 5-task.
#def daraja(x,y):
 #  print(f"{x} ning {y}-darajasi {x**y} ga teng")
#daraja(99,9)
#def daraja(x,y=2):
 #   """X ning Y inchi darajasini hisoblaydigan funksiya """
  #  print(f"{x} ning {y}-darajasi {x**y} ga teng")
#daraja(99)

# Funksiya 6-task.
def qolsizbol (x):
 for n in range(2,10):
   if x % n==0:
      print(f"{x} {n} ga qoldiqsiz bo`linadi.")
qolsizbol(270)