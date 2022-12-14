import matplotlib.pyplot as plt

X = range(100)
plt.plot(X, [x*x for x in X])
plt.show()
