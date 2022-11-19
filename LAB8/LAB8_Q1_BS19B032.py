import numpy as np
import matplotlib.pyplot as plt
import math

#plotting given surface

w1 = np.linspace(-10,10,1000)
w2 = np.linspace(-10,10,1000)
W1,W2 = np.meshgrid(w1,w2)
J = (W1-10)**2 + (W2-10)**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(W1, W2, J)
ax.set_xlabel('W1')
ax.set_ylabel('W2')
ax.set_zlabel('J(W1,W2)')
ax.set_title('Curved Sheet')
plt.show()

fig1,ax1 = plt.subplots()
CS = ax1.contour(W1,W2,J)
ax1.clabel(CS,inline=True,fontsize=10)
ax1.set_xlabel('W1')
ax1.set_ylabel('W2')
ax1.set_title('Contour plot of curved sheet')
plt.show()
