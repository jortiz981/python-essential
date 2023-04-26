# -*- coding: utf-8 -*-
"""
Created on Wed May 13 19:48:17 2020

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
print(titulos[titulos.title.str.contains("The Lord of the Rings")].sort_values('year'))
print(titulos[titulos.title== "Dracula"].sort_values("year"))
print(titulos[titulos.title.str.contains("Exorcist")].sort_values('year'))
print( elenco[elenco.title == "The Godfather"] )
print( elenco[elenco.name == "Hugh Jackman"] )
print( elenco[elenco.character == "Hulk"] )
print( elenco[elenco.character == "Superman"] )
c = elenco
print( c[c.name == "Hugh Jackman"].sort_values("year"))
print( titulos[ (titulos.year >= 1950) & (titulos.year <= 1960) ] )