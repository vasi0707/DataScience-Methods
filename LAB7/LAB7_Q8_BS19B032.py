import numpy as np
import matplotlib.pyplot as plt
import math

#plotting cone

x = np.linspace(-10,10,1000)
y = np.linspace(-10,10,1000)
X,Y = np.meshgrid(x,y)
z = np.sqrt((X**2+Y**2)/2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Cone')
plt.show()

fig1 = plt.figure()
axes = fig1.gca(projection ='3d')
axes.contour(X,Y,z)
plt.show()
