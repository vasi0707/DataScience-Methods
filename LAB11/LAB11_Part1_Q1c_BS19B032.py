import math
import matplotlib.pyplot as plt
import numpy as np

def sigmoid(x):
    ans = ((math.e)**x)/((math.e)**x+ 1)
    return ans

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

x = [1.2,2.3,4.5,6.7,5.6,7.8,3.2,4.5,2,5.6]

y = [1,1,1,0,0,1,1,0,1,0]

alpha = 0.0001

y = np.array(y)

n = 1
m = len(x)

ans,var = linear_regression(x,y,n,m,alpha)

print("The weights are:")
print(ans)

h_w = np.matmul(np.transpose(ans),var)
plt.scatter(x,y,color='orange')
plt.plot(x,h_w)
plt.title("Linear Regression")
plt.show()

x1 = np.linspace(-10,10,100)
X,Y = np.meshgrid(x1,y)
z = (1/2*m)*(ans[0] + ans[1]*X - Y)**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Cost Function')
plt.show()

fig1 = plt.figure()
axes = fig1.gca()
axes.contour(X,Y,z)
plt.show()

entropy = []

for i in range(len(x)):
    wt = np.transpose(ans)@[1,x[i]]
    cost = ((-1)*y[i]*math.log(sigmoid(wt))) - ((1-y[i])*(math.log(1-sigmoid(wt))))
    entropy.append(cost)

fig2 = plt.figure()
ax = plt.axes(projection = '3d')
X,Y = np.meshgrid(x,y)
cost = ((-1)*Y*math.log(sigmoid(sum(sum(ans[0]+ans[1]*X))/100))) - ((1-Y)*(math.log(1-sigmoid(sum(sum(ans[0]+ans[1]*X))/100))))

ax.plot_surface(X,Y,cost)
ax.set_title("Cost Function")
plt.show()

fig1 = plt.figure()
axes = fig1.gca()
axes.contour(X,Y,cost)
plt.show()
