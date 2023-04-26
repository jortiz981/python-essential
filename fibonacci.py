# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 14:04:23 2023

@author: juan.ortiz
"""

def fibonacci(n):
    a, b = 0,1
    while a <= n:
        print(a, end=' ')
        #c=a+b
        #a=b
        #b=c
        a, b = b, a+b
print()
#fibonacci(8)