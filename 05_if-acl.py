# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 12:37:02 2023

@author: juan.ortiz
"""

acl=int(input("Ingrese el # de ACL: "))
if acl>=1 and acl<=99:
    print("LA ACL es estandar")
elif acl>=100 and acl<=199:
    print("LA ACL es extendida")
else:
    print("No es un # de ACL")