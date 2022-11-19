import math
import matplotlib.pyplot as plt
import numpy as np

def sigmoid(x):
    ans = ((math.e)**x)/((math.e)**x+ 1)
    return ans

x = np.linspace(-2,2,1000)

y1 = []
y2 =[]

for i in x:
    val1 = (-1)*(math.log(sigmoid(i)))
    val2 = (-1)*((math.log(1-sigmoid(i))))
    y1.append(val1)
    y2.append(val2)

plt.plot(x,y1)
plt.xlabel("X")
plt.ylabel("-log(z)")
plt.title("-log(z) Function")
plt.show()

plt.plot(x,y2)
plt.xlabel("X")
plt.ylabel("-log(1-z)")
plt.title("-log(1-z) Function")
plt.show()

print("The two log functions are log loss functions, which calculates the log loss for each variable, when it is classified as 1 and 0.")
