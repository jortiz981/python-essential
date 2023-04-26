# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 00:27:16 2023

@author: juan.ortiz
"""

try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")
print("THE END.")