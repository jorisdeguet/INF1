import csv
import numpy as np
from numpy.polynomial import Chebyshev
import matplotlib.pyplot as plt

times = []
heights = []

with open('demo-csv/data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        times.append(float(row[0])/120)
        heights.append(float(row[1])*2.54)

print(times)
print(heights)

x = np.array(times)
y = np.array(heights)

speeds = [0]
for i in range(1, len(x)):
    speed = (y[i] - y [i-1]) / (x[i] - x[i-1]) /10.0
    speeds.append(speed)
print(speeds)

# calcul une approx polynomial de y en x^i i allant jusqu'à 3
deg1 = np.polyfit(x, y, 1)
p1 = np.poly1d(deg1)       # créé une série affichable sur le plot
deg2 = np.polyfit(x, y, 2)
p2 = np.poly1d(deg2)
print("--------------------------")
print(p1)
print("--------------------------")
print("--------------------------")
print(p2)
print("--------------------------")

vitesse = np.polyint(p2)
#print(vitesse)
accel = np.polyint(vitesse)
#print(accel)
acc = np.poly1d(accel)

xp = np.linspace(0, 5, 300)

plt.plot(x, speeds, '.')
plt.plot(x, y, '.')
plt.plot(x, p2(x), '-', x, vitesse(x), '--', x, accel(x), '--')
plt.show()

