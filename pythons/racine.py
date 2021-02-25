# coder un script qui utilise
# le fait que racine carré soit monotone
# et la force brute pour calculer la racine carrée d'un nombre

def milieu(a,b):
  return (a+b+0.0) / 2;

def carre(a):
  return a*a;

cible = 6174.0;

a = 0;
b = cible;
delta = 0.000001;

while abs(carre(milieu(a,b)) - cible) > delta :
  print(str(a) + ' ' + str(b) + ' ' + str(a*a));
  if (carre(milieu(a,b)) > cible):
    b = milieu(a,b);
  else:
    a = milieu(a,b);

print(milieu(a,b));
print(carre(milieu(a,b)));
print(cible);