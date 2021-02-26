import math

# conversions string float int

entier = 5
texte = "5"

print(texte+"5")          # + pour un texte, c'est concaténer : mettre à la suite "5"+"5" = "55"
print(entier+5)           # + pour des entiers c'est l'addition

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