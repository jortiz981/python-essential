# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 15:46:33 2023

@author: juan.ortiz
"""

file = open("devices.txt", "a")
while True:
    newItem = input("Ingrese nuevo dispositivo: ")
    if newItem == "exit":
        print("Ok!")
        break
    file.write(newItem + "\n")
file.close()
