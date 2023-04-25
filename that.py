# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 07:35:38 2023

@author: juan.ortiz
"""

d = {'k1':['val1','val2','val3',{'we':['need','to','go',{'deeper':[1,2,3,'that']}]}]}

print(d['k1'][3]['we'][3]['deeper'][3])
