# demo de liste, construction, iteration, affichage

liste = []                          # crée une liste vide
liste.append(3)                     # ajoute une valeur à la fin de la liste
liste.append(5)
liste.append(9)
liste.append(11)
print(liste)                        # affiche la liste
print('longueur : fonction len()  ', len(liste))

print(liste[0])                     # les indices commencent à 0
print(liste[ len(liste) - 1 ])      # les indices et finissent à longueur - 1

liste[1] = 7                      # remplace dans la liste à la position 1 (le deuxième)
print(liste)

liste.insert(0, 1)                  # on peut insérer une valeur à une position, ici à l'indice 0 donc au début
print(liste)

liste.pop()                         # permet de supprimer le dernier élément
print(liste)

del liste[0]                        # permet de supprimer n'importe quel élément de la liste
print(liste)

# parcours de chaque valeur dans l'ordre de la liste
for element in liste:
    print(element)
# utiliser les indices explicites pour par exemple, enumérer tous les couples
for i in range(0, len(liste)):
    for j in range(i+1, len(liste)):
        elementI = liste[i]
        elementJ = liste[j]
        print(i, ' -> ', elementI, '     ', j, ' -> ', elementJ)




