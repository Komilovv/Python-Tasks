# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 20:52:05 2023

@author: ADMIN
"""

davlatlar ={'Uzbekistan':{'currency':'so`m',
                          'population':'36 million',
                          'type':'democracy only in the paper'},
            'UK':{'currency':'GBP',
                  'population':'67 million',
                  'type':'kingdom'},
            'South Korea':{'currency':'won',
                  'population':'51 million',
                  'type':'democracy'}}
for ism , info in davlatlar.items():
    print(f"\n{ism}ning pul birligi {info['currency']},"
          f"\naholi soni {info['population']},"
          f"\nboshqaruv turi esa {info['type']}")