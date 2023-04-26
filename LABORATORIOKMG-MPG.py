# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 10:43:37 2023

@author: jorti
"""

def l100kmtompg(liters):
    mpg = 235.214583 / liters
    return mpg

def mpgtol100km(miles):
    l100km = 235.214583 / miles
    return l100km


print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))