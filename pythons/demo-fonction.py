

# on definit une fonction dont le nom est ma_fonction
# elle prend 3 parametres a b et c
# quand on appelle la fonction, il faut donner les valeurs de a b et c
def ma_fonction(a,b,c):
    # on peut écrire ici le code de la fonction
    # le tout doit etre indenté d'un niveau
    # on peut mettre un point d'arret dans ce code pour déboguer
    mavariable = a + b
    # le mot clé return indique qu'on renvoie le résultat
    # cela met fin a la methode et nous renvoie au point
    # ou la methode a été appelée avec la valeur de l'expression
    return 10 * mavariable

# dans le programme on va appeler la fonction
# il suffit d'écrire son nom suivi des valeurs pour les parametres
# entre parentheses

# ici on appelle la fonction avec 3 comme valeur pour a
# 5.0 pour b et 12 pour c
# "ma_fonction(3, 5.0, 12) est une expression dont la valeur est
# le return de ma_fonction
mon_resultat = ma_fonction(3, 5.0, 12)
print(mon_resultat)

# les parametres ne sont pas forcement des constantes
# elles peuvent etre n'importe quelle expression
a = 120
autre_resultat = ma_fonction(a, ma_fonction(1,2,3), (5+9))
print(autre_resultat)