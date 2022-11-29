import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# on définit une fonction de x avec 3 paramètres qui pourraient varier
# il s'agit plutôt d'une forme de fonction
def func(x, a, b, c):
  return a * np.exp(-b * x) + c

# on produit une série de x
xdata = np.linspace(0, 4, 50)
# on produit une série de func(x)
y = func(xdata, 2.5, 1.3, 0.5)
# on met un peu de bruit aléatoire sur les données pour pimenter le tout
rng = np.random.default_rng()
y_noise = 0.2 * rng.normal(size=xdata.size)
ydata = y + y_noise

plt.plot(xdata, ydata, 'b-', label='data')

popt, pcov = curve_fit(func, xdata, ydata)
print(popt)

plt.plot(xdata, func(xdata, *popt), 'r-', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()