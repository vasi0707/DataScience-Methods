import math
import matplotlib.pyplot as plt
import numpy as np

def sigmoid(x):
    ans = ((math.e)**x)/((math.e)**x+ 1)
    return ans

x = np.linspace(-10,10,1000)

y = []

for i in x:
    y.append(sigmoid(i))

plt.plot(x,y)
plt.xlabel("X")
plt.ylabel("Sigma")
plt.title("Sigmoid Function")
plt.show()

print("In classification problems, the sigmoid function is used to predict the probability of given variable. As the sigmoid function is bound between 0 to 1, it is widely used logistic function.")

