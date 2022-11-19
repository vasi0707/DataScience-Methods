import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

def grad(h,weights,var):
    diff = h-y
    for i in range(len(weights)):
        p = 0
        for j in range(m):
            p += (1/m)*(diff[j])*var[i][j]
        weights[i] = weights[i] - alpha*p
        
    return weights

def steepest_gradient_descent(weights,var,y,m,n):
    Iterations = 100000
    count = 0

    while(count<=Iterations):
        h = np.matmul(np.transpose(weights),var)
        J = (1/(2*m))*np.sum((h-y)**2)
        weights = grad(h,weights,var)
        count += 1

    return weights

def linear_regression(x,y,n,m,alpha):
    weights = [1.0]*(n+1)
    weights = np.array(weights)
    var = [1]*m
    var = [*var,*x]
    var = np.array(var)
    var = var.reshape(n+1,m)
    ans = steepest_gradient_descent(weights,var,y,m,n)

    return ans,var

alpha = 0.0001

file = pd.read_csv('heart.data.csv')

w1 = file['biking']
w2 = file['smoking']
y = file['heart.disease']
y = np.array(y)

n = 2
m = len(w1)

x = np.array([*w1,*w2])

ans,var = linear_regression(x,y,n,m,alpha)

print("The weights are:")
print(ans)

x1 = np.linspace(-10,10,100)
y1 = np.linspace(-10,10,100)
X,Y = np.meshgrid(x1,y)
z = ans[0] + ans[1]*X + ans[1]*Y

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, z)
ax.set_xlabel('Biking')
ax.set_ylabel('Smoking')
ax.set_zlabel('Heart Disease')
ax.set_title('Heart Data: Multivariate Linear Regression')
plt.show()
