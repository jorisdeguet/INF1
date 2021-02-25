import csv
import numpy as np
import matplotlib.pyplot as plt

with open('data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:

        print('.... '.join(row))


x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([0.0, 0.8, 0.9, 0.1,-0.8,-1.0])

z = np.polyfit(x, y, 3)

p30 = np.poly1d(np.polyfit(x, y, 30))

p = np.poly1d(z)
xp = np.linspace(-2, 6, 100)

_ = plt.plot(x, y, '.', xp, p(xp), '-', xp, p30(xp), '--')
plt.ylim(-2,2)
(-2, 2)
plt.show()

