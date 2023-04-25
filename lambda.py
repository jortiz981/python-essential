# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 18:01:40 2023

@author: juan.ortiz
"""

seq = ['data','salt' ,'dairy','cat', 'dog']
resultado = list(filter(lambda word: word[0] == 'd', seq))
print(resultado)