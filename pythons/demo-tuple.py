print("------------------------------------------")
# un tuple c'est plusieurs valeurs mises ensemble par forcément du même type
a = (4, 5, " test")
print(a)
print(a[0]) # le premier element du tuple
print(a[1])
print(a[2])
print(len(a)) # le nombre d'elements dans le tuple

print("------------------------------------------")
# prend le premier morceau de a le met dans x, le 2eme dans y et le 3eme dans y
(x, y, y) = a
print(x)
print(y)

print("------------------------------------------")
(x, y, z) = a
print(x)
print(y)