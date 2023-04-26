# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:23:07 2020

@author: Juan Carlos
"""
import pandas as pd
titulos = pd.read_csv('data/titles.csv' )
print(titulos.head(5))
print("\n"*2)
elenco = pd.read_csv('data/cast.csv', encoding='utf-8')
print(elenco.head(5))
print("\n"*2)
print(len(titulos))
print("\n"*2)
print ((len(elenco)))
print("\n"*2)
# Cual fue la primer pelicula hecha titulada "Romeo and Juliet" ?
print(titulos[titulos.title == "Romeo and Juliet"].sort_values('year').head(20))
print(titulos[titulos.title.str.contains("lord")].sort_values('year'))