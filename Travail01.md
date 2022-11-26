# Calcul de la racine d'un nombre, stupide et brutale

L'ordinateur est stupide mais très rapide. On va calculer la racine
avec une méthode très lente et stupide ce qui est parfait pour un ordinateur.

### méthode 1, chiffre par chiffre, par en dessous

Un exemple sur la racine carrée de 8:

**unité :**  
- 0 : 0 * 0 = 0
- 1 : 1 * 1 = 1
- 2 : 2 * 2 = 4
- 3 : 3 * 3 = 9

Comme **8** est entre 4 et 9, on sait que la racine de 8 
est entre 2 et 3: 2,...

On valide 2 comme chiffe des unités.

**première décimale**
- 2,0 * 2,0 = 4
- 2,1<sup>2</sup> = 4,41
- 2,2<sup>2</sup> = 4,84
- 2,3<sup>2</sup> = 5,29
- 2,4<sup>2</sup> = 5,76
- 2,5<sup>2</sup> = 6,25
- 2,6<sup>2</sup> = 6,76
- 2,7<sup>2</sup> = 7,29
- 2,8<sup>2</sup> = 7,84
- 2,9<sup>2</sup> = 8,41

La racine de 8 ressemble à 2,8.... 8 sera le chiffre des dixième.

**2ème décimale**
- 2,80<sup>2</sup> = 7,84
- 2,81<sup>2</sup> = 7,8961
- 2,82<sup>2</sup> = 7,9524
- 2,83<sup>2</sup> = 8,0089

Racine de 8 est de la forme 2,82...

### méthode 2 : dichotomie (couper en 2)
On commence avec racine carrée de 8 doit être entre 0 et 8, on va essayer de resserrer cet interval jusqu'à trouver la racine
- [0 .. 8] le milieu est : 4 * 4 = 16
- on doit décider si la racine de 8 est dans [0 .. 4] ou [4 .. 8], comme 16 est au dessus de 8, la racine de 8 doit être entre 0 et 4
- [0 .. 4] le milieu est 2 : 2 * 2 = 4
- Comme 4 est en dessous de 8, le résultat est dans la moitié haute [2 .. 4]
- [2 .. 4] 3<sup>2</sup> = 9 donc [2 .. 3] 
- [2 .. 3] 2,5<sup>2</sup> = 6,25 donc [2,5 .. 3] 
- [2,5 .. 3] 2,75<sup>2</sup> = 7,5625 donc [2,75 .. 3] 
- [2,75 .. 3] 2,875<sup>2</sup> = 8.265625 donc [2,75 .. 2,875] 
- etc. 

## Calcul de la racine carrée

En utilisant le principe de ton choix, tu dois produire un script
appelé racineCarree*NomDeFamille*.py dans lequel on trouvera une fonction
```python
def racineCarre(nombre: float) -> float:
  #ton code ici
  return racine
```
Vous devrez aussi montrer les appels de cette méthode sur les nombre 0 0,1 0,2 0,9 8 9 81 123 et -3.

- **1 point** le fichier existe, son nom respecte la consigne, il contient la fonction demandée et n'a pas d'erreur de syntaxe
- **2 points** les racines carrées affichées pour 0 0,1 0,2 0,9 8 9 81 123 sont bonnes à 0,001 près.
- **1 point** l'appel pour le nombre négatif lance une exception