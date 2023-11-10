# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 21:57:12 2023

@author: ADMIN
"""

#def kopaytir(*sonlar):
 #   while True:
  #      kopaytma =1
   #     for n in sonlar:
    #       kopaytma= kopaytma*n
     #   return kopaytma 
#kopaytir(2,4,8,5)
def talaba_info(ism, familiya,** other):
    other["Ismi"]=ism
    other["Familiyasi"]=familiya
    return other
print(talaba_info('Otabek','Komilov',tyil=2005,major ='AI'))