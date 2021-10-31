# montrer que immutable pour changer de valeur ca prend une autre assign
# mutable peut changer de valeur sans avoir de nouvelle assignation

# un type immutable ne peut pas changer de valeur (int float string ...)
# donc tant que je ne réassigne pas de nouvelle valeur, ma variable ne change pas
immutableEntier = 5
print(immutableEntier)

# les opérateurs sur les types immutables ne change pas les opérandes
# mais renvoie plutot un nouvel objet
immutableString = "coucou"
copie = immutableString
print(immutableString)
immutableString + " le monde"
print("immutable String n'a pas changé                    " + immutableString)
# pour récupérer la nouvelle valeur, il faut une nouvelle affectation
# il faut lire de la droite vers la gauche
# on commence par évaluer : immutableString + " le monde"
# comme immutableString vaut "coucou", ca fait "coucou" + " le monde" > "coucou le monde"
# on assigne cette nouvelle valeur dans immutableString
immutableString = immutableString + " le monde"
print("immutable String reassigné                         " + immutableString)
print("la copie a toujours la meme valeur                 " + copie)


print("\n\n--------------------------------------------------------------------------------------\n\n")

# un type mutable peut changé sans être réassigné
mutable = ["yo", "mama", "lit"]
print("valeur de liste au début                           " + str(mutable))
autre = mutable
mutable.append("coucou")
print("mutable a été changé sans reassignation            " + str(mutable))
print("autre aussi                                        " + str(autre))