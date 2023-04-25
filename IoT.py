# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 09:59:12 2023

@author: juan.ortiz
"""

def countIoT(st):
    count = 0
    iot = 'IoT'
    for i in range(len(st)):
        if iot in st[i:].lower():
            count += 1
    return count