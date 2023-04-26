# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 13:36:49 2023

@author: juan.ortiz
"""

lista=[]
file=open("devices.txt")
for item in file:
    item=item.strip()
    lista.append(item)
    #print(item)
file.close()
print(lista)