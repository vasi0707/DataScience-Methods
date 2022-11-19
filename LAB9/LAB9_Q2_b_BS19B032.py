import numpy as np
import matplotlib.pyplot as plt
import math

def func(x,y):
    ans = (x-10)**2 + (y-10)**2
    return ans

def grad(x,y):
    grad1 = 2*x - 20
    grad2 = 2*y - 20

    return grad1,grad2

def mod(J):
    ans = math.sqrt(J[0]**2 + J[1]**2)
    return ans

def bracketing(a,b,n,direction):
    del_w = (b-a)/n
    w1 = a
    w2 = a + del_w
    w3 = w2 + del_w

    flag = 0

    while w3<=b:
        p1 = start_points + w1*direction
        p2 = start_points + w2*direction
        p3 = start_points + w3*direction
        J1 = func(*p1)
        J2 = func(*p2)
        J3 = func(*p3)
        if((J1>=J2) and (J2<=J3)):
            break
        else:
            w1 = w2
            w2 = w3
            w3 = w3 + del_w
    return w2

def steepest_gradient_descent(x,y,a,b):
    Iterations = 10000
    count = 0

    J = grad(x,y)
    mod_J = mod(J)

    points = [[x,y]]

    while((count<=Iterations) and (mod_J>=0.05)):
        J1 = np.array(grad(x,y))
        alpha = bracketing(a,b,1000,J1)
        x = x - (alpha*J1[0])
        y = y - (alpha*J1[1])
        points.append([x,y])
        J2 = np.array(grad(x,y))

        if(abs(np.dot(J1,J2))<=0.005):
            break
        count += 1

    return x,y,count,points

start_points = np.array([2,1])

a = 0.05
b = 1

x1,y1,iterations,points = steepest_gradient_descent(*start_points,a,b)

print("The minimum point found by steepest gradient method at fixed alpha is: ")
print(x1,y1)
print("")
print("The number of iterations is:")
print(iterations)
print("")
print("The points that were iterated:")
print(points)

p = zip(*points)
q = [*p]

x = np.linspace(0,15,100)
y = np.linspace(0,15,100)
X,Y = np.meshgrid(x,y)
z = (X-10)**2 + (Y-10)**2

fig1 = plt.figure()
axes = fig1.gca()
axes.contour(X,Y,z)
axes.plot(x1,y1,'r',marker="o")
axes.plot(q[0],q[1],'orange',marker="x")
plt.show()
