import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

def grad(h,weights,var,y):
    diff = h-y
    for i in range(len(weights)):
        p = 0
        for j in range(m):
            if i==0:
                p += (1/m)*(diff[j])*var[i][j]
            else:
                p += (1/m)*((diff[j])*var[i][j] + (lda*weights[i]))
        weights[i] = weights[i] - alpha*p
        
    return weights

def steepest_gradient_descent(weights,var,y,m,n):
    Iterations = 100000
    count = 0

    while(count<=Iterations):
        h = np.matmul(np.transpose(weights),var)
        weights = grad(h,weights,var,y)
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
lda = 0.01

file = pd.read_csv('univariate_linear_regression.csv')

x = file['x']
y = file['y']
y = np.array(y)

x_train = []
y_train = []
x_test = []
y_test = []

split = int(len(x)*0.7)

for i in range(len(x)):
    if(i<split):
        x_train.append(x[i])
        y_train.append(y[i])
    else:
        x_test.append(x[i])
        y_test.append(y[i])

n = 1
m = len(x_train)

ans,var = linear_regression(x_train,y_train,n,m,alpha)

print("The weights are:")
print(ans)

weights = [1.0]*(n+1)
weights = np.array(weights)
var1 = [1]*(len(x_test))
var1 = [*var1,*x_test]
var1 = np.array(var1)
var1 = var1.reshape(n+1,(len(x_test)))

h_w = np.matmul(np.transpose(ans),var)
h_w1 = np.matmul(np.transpose(ans),var1)

mse = 0

for i in range(len(y_test)):
    mse += (y_test[i]-h_w1[i])**2

error = mse/(len(y_test))

print("The test error is:")
print(error)
plt.scatter(x_train,y_train,color='orange')
plt.plot(x_train,h_w,color='blue')
plt.title("Train Data")
plt.show()
plt.scatter(x_test,y_test,color='green')
plt.plot(x_test,h_w1,color='red')
plt.title("Test Data")
plt.show()
