# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 07:45:28 2023

@author: juan.ortiz
"""

def GetDomain(email):
    """
    Toma el dominio del sitio web de correo electrónico de una cadena en la forma: 'user@domain.com'.
    """
    # Dividir la cadena en dos partes usando el caracter '@' como separador
    parts = email.split('@')
    # La última parte es el dominio
    domain = parts[-1]
    return domain

# en la consola poner GetDomain('user@domain.com') y poner enter.