import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

def sigmoid(mat):
    ans = []
    for x in mat:
        ans.append(((math.e)**x)/((math.e)**x+ 1))
    return ans

def grad(hw,weights,var):
    diff = hw-y
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
        hw = sigmoid(h)
        weights = grad(hw,weights,var)
        count += 1
        
    return weights

def logistic_regression(x,y,n,m,alpha):
    weights = [1.0]*(n+1)
    weights = np.array(weights)
    var = [1]*m
    var = [*var,*x]
    var = np.array(var)
    var = var.reshape(n+1,m)
    ans = steepest_gradient_descent(weights,var,y,m,n)

    return ans

alpha = 0.0001

file = pd.read_csv('Logistic_regression_ls.csv')

w1 = file['x1']
w2 = file['x2']
y = file['label']
y = np.array(y)

n = 2
m = len(w1)

x = np.array([*w1,*w2])

ans = logistic_regression(x,y,n,m,alpha)

print("The weights are:")
print(ans)

x1 = []
y1 = []
x2 = []
y2 = []

x_line = np.linspace(0,10,10)
x_line1 = np.linspace(0,10,10)
y_line = []

for i in x_line:
    val = (0.5 - ans[0] - (ans[1]*i))/(ans[2])
    y_line.append(val)

for i in range(len(y)):
    if y[i]==0:
        x1.append(w1[i])
        y1.append(w2[i])
    else:
        x2.append(w1[i])
        y2.append(w2[i])

plt.scatter(x1,y1,color = 'blue')
plt.scatter(x2,y2,color = 'orange')
plt.plot(x_line,y_line,color = 'green')
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Logistic Regression')
plt.show()
