import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# on définit une fonction de x avec 3 paramètres qui pourraient varier
# il s'agit plutôt d'une forme de fonction
def func(x, a, b, c, d, e):
  return a * np.exp(-b * x) + c + d*x*x + e*x

# on produit une série de x
xdata = np.linspace(1, 4, 100)
# on produit une série de func(x)
y = func(xdata, 2.5, 1.3, 0.5, 0, 0)
# on met un peu de bruit aléatoire sur les données pour pimenter le tout
rng = np.random.default_rng()
y_noise = 0.1 * rng.normal(size=xdata.size)
ydata = y + y_noise
print(ydata)
plt.plot(xdata, ydata, 'b-', label='data')

popt, pcov = curve_fit(func, xdata, ydata, maxfev=200000)
print(popt)

plt.plot(xdata, func(xdata, *popt), 'r-', label='fit: a=%5.3f, b=%5.3f, c=%5.3f, d=%5.3f, e=%5.3f' % tuple(popt))

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()