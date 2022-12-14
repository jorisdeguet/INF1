import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

w = 3
Y, X = np.mgrid[-w:w:100j, -w:w:100j]
U = -1 - X**2 + Y
V = 1 + X - Y**2
speed = np.sqrt(U*U + V*V)

fig = plt.figure(figsize=(14, 18))
gs = gridspec.GridSpec(nrows=3, ncols=2, height_ratios=[1, 1, 2])

grains = 10
tmp = tuple([x]*grains for x in np.linspace(-2, 2, grains))
xs = []
for x in tmp:
    xs += x
ys = tuple(np.linspace(-2, 2, grains))*grains


seed_points = np.array([list(xs), list(ys)])
# Varying color along a streamline
ax1 = fig.add_subplot(gs[0, 1])

strm = ax1.streamplot(X, Y, U, V, color=U, linewidth=np.array(5*np.random.random_sample((100, 100))**2 + 1), cmap='winter', density=10,
                      minlength=0.001, maxlength = 0.07, arrowstyle='fancy',
                      integration_direction='forward', start_points = seed_points.T)
fig.colorbar(strm.lines)
ax1.set_title('Varying Color')

plt.tight_layout()
plt.show()

#https://problemsolvingwithpython.com/06-Plotting-with-Matplotlib/06.15-Quiver-and-Stream-Plots/
ax = plt.figure().add_subplot(projection='3d')

# Make the grid
x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.8))

# Make the direction data for the arrows
u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
     np.sin(np.pi * z))

ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)

plt.show()