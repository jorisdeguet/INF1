# coding: utf-8

import math
import sys

# conversions string float int

# définition d'une variable dont le nom est entier
entier = 5
texte = "5"

print(texte + "5")          # + pour un texte, c'est concaténer : mettre à la suite "5"+"5" = "55"
print(entier + 5)           # + pour des entiers c'est l'addition
print(bin(entier+5))


print(type(texte))          # str pour string ou chaine de caractères en français
print(type(entier))         # int pour integer ou nombre entier

flottant = float(entier)
flottant = flottant * math.pi
print('exemple flottant mult par Pi ',flottant)
# convertit un entier en nombre flottant
entier = int(flottant)
print('exemple entier mult par Pi ',entier)

texte = str(flottant)
print('exemple texte: ',texte)

flottant = float(texte)
print('exemple flottant: ',flottant)

entier = int(flottant)
print('convertir en entier ca change quoi: ',entier)

print("++++++++++++++++++++++++++")
print(type(5))
print(type("coucou"))
print(type(3.6e123))
print(type(3.5))
print("++++++++++++++++++++++++++")

print(sys.int_info.bits_per_digit)
print(sys.float_info.max)
