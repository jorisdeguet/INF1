# coding: utf-8

# TODO ils ont tu math fortes

# 1 point lire le fichier CSV
# 2 points afficher le nuage de points

# 3 points pour les degrés 0 1 2 3 4 5 approximer un
# polynomes et l'afficher dans console

# 2 points afficher les differentes approx dans un plot avec le nuage

# 2 points pour chaque poly calculer l'erreur d'approximation

# 3 points émettre une hypothèse sur l'équation reliant energie et vitesse

# lire des données et extrapoler
import copy
import csv

import numpy as np
#import scipy as sp
from matplotlib import pyplot as plt

x = []
y = []
with open('../energeie.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:
        print("colonne 1 : " + (row[0])  + "  colonne 2 : " + (row[1]))
        x.append(float(row[0]))
        y.append(float(row[1]))


#plt.plot(x, [e*e*10/2 for e in x])
plt.scatter(x, y)
plt.show()

for degre in range(0,6):
    z = np.polyfit(x, y, degre)
    p = np.poly1d(z)
    print("---------------------------------")
    print("approximation polynomial de degre " + str(degre))
    print(p)
    sorted = copy.deepcopy(x)
    sorted.sort()
    plt.plot(sorted, [p(e) for e in sorted])
plt.show()

#scipy.optimize.curve_fit(lambda t,a,b: a+b*numpy.log(t),  x,  y)