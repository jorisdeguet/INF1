# https://stackoverflow.com/questions/3433486/how-to-do-exponential-and-logarithmic-curve-fitting-in-python-i-found-only-poly
# different fits poly, log, sin
# from scipy.optimize import curve_fit

import random

csv = ""
for i in range(1,50):
    vitesse = random.random() * 1000
    masse = 10
    energie = masse / 2 * vitesse * vitesse
    energiebruitee = energie * (1 + random.random()/6)
    csv += str(vitesse) + ";" + str(energiebruitee) +";"+str(masse) +  ";\n"

print(csv)

with open('energeie.csv', 'w') as f:
    f.write(csv)