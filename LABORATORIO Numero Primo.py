# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 08:17:05 2023

@author: jorti
"""

def isPrime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

for i in range(1, 20):
    if isPrime(i + 1):
        print(i + 1, end=" ")
print()