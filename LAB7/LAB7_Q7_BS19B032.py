import matplotlib.pyplot as plt
import numpy as np
import math

#plotting sin function

x = np.linspace(-10,10,10000)
y = [*(map(lambda a:math.sin(a),x))]

plt.plot(x,y,color='blue',linewidth=2)
plt.plot([0]*10000,y,color='green',linewidth=3)
plt.plot(x,[0]*10000,color='green',linewidth=3)
plt.xlabel("X")
plt.ylabel("Sin(X)")
plt.title("SinX function")
plt.show()

#plotting cos function

x = np.linspace(-10,10,10000)
y = [*(map(lambda a:math.cos(a),x))]

plt.plot(x,y,color='blue',linewidth=2)
plt.plot([0]*10000,y,color='green',linewidth=3)
plt.plot(x,[0]*10000,color='green',linewidth=3)
plt.xlabel("X")
plt.ylabel("Cos(X)")
plt.title("CosX function")
plt.show()

#plotting user defined function
def func(x):
    y = x**3 - x**2 + x + 10
    return y

x = np.linspace(-10,10,10000)
y = [*(map(lambda a:func(a),x))]

plt.plot(x,y,color='blue',linewidth=2)
plt.plot([0]*10000,y,color='green',linewidth=3)
plt.plot(x,[0]*10000,color='green',linewidth=3)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Function: x**3 - x**2 + x + 10")
plt.show()
