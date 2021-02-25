import csv
import numpy as np
from numpy.polynomial import Chebyshev
import matplotlib.pyplot as plt

times = []
heights = []

with open('data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        times.append(float(row[0]))
        heights.append(float(row[1]))

print(times)
print(heights)

x = np.array(times)
y = np.array(heights)

# calcul une approx polynomial de y en x^i i allant jusqu'à 3
deg3 = np.polyfit(x, y, 1)
p3 = np.poly1d(deg3)       # créé une série affichable sur le plot

deg4 = np.polyfit(x, y, 2)
p4 = np.poly1d(deg4)

xp = np.linspace(0, 5, 300)

plt.plot(x, y, '.')
plt.plot(x, p4(x), '-', x, p3(x), '--')
plt.show()

