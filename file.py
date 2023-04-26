# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 14:00:04 2023

@author: juan.ortiz
"""


file=open("devices.txt")
for item in file:
    item=item.strip()
    print(item)
file.close()
