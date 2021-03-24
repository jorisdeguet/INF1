# calculer pi avec seulement des opération de base
import math
import time
import multiprocessing as mp

# version simple A : on calcule plein de points et on compte ceux dans le quart de cercle
def computePi(nombreDeDivision):
    coords = range(0, nombreDeDivision)
    step = 1.0 / nombreDeDivision
    compteurInterieur = 0
    compteurTotal = nombreDeDivision * nombreDeDivision     # tous les points de la grille = nombreDeDivision^2
    for i in coords:
        x = i * (step)
        for j in coords:
            y = j * (step)
            if (x**2 + y**2) <= 1:               # test de intérieur du cercle
                compteurInterieur = compteurInterieur + 1
    return 4 * (compteurInterieur / compteurTotal)

def calculDansCercleUneRangee(i, coords, step):
    compteur = 0
    x = i * (step)
    for j in coords:
        y = j * (step)
        if (x ** 2 + y ** 2) <= 1:  # test de intérieur du cercle
            compteur = compteur + 1
    return compteur

# version simple A : on calcule plein de points et on compte ceux dans le quart de cercle
def computePiParallele(nombreDeDivision):
    pool = mp.Pool(mp.cpu_count())
    coords = range(0, nombreDeDivision)
    step = 1.0 / nombreDeDivision
    resultats = [pool.apply(calculDansCercleUneRangee, args=(i, coords, step)) for i in coords]
    pool.close()
    return 4 * (sum(resultats) / (nombreDeDivision * nombreDeDivision))

def main():

    for i in range(1, 5000, 100):
        a = time.time();
        pi = computePi(i)
        b = time.time()  # calcul du temps de calcul de la fonction
        pi2 = computePiParallele(i)
        c = time.time();
        print(i, ' dalles : ', pi, ' @ ', (b-a), '   ', pi2, ' @ ', (c-b))

if __name__ == "__main__":
    main()

