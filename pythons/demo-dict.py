person = {
    "firstName": "John",
    "lastName": "Doe",
    "age": 28
}

# un dictionnaire peut être vu comme un tuple où on donne des noms à chaque morceau
print("a quoi ca ressemble dans un print")
print(person)
print("comment accéder juste un morceau")
print(person["age"])


print("quel est son type")
print(type(person))
# la question qui vrille le cerveau, c'est quoi le type d'un type
print("quel est le type de son type")
print( type( type(person) ) )