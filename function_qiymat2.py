# -*- coding: utf-8 -*-

#def eng_katta(a,b,c):
 #   """Uchta son qabul qilib eng kattasini qaytaradigan funksiya"""
  #  max = a
   #   max=b
    #if c>=max:
 #      max=c
    #return max
#big=eng_katta(467,8564,2598)
#print(big)
def aylana_info(r):
    """Aylananing r,d,p,S ni lug'at ko'rinishida chiqaradi"""
    PI=3.14
    aylana={'radiusi':r,
            'Diametri':2*r,
            'Perimetri':2*r*PI,
            'Yuzasi':PI*r**2}
    return aylana 
aylana_info(12)
