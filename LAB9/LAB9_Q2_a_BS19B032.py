import numpy as np
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

def steepest_gradient_descent(x,y,a,b):
    Iterations = 100000
    count = 0

    J = grad(x,y)
    mod_J = mod(J)

    while((count<=Iterations) and (mod_J>=0.005)):
        J1 = np.array(grad(x,y))
        x = x - (alpha*J1[0])
        y = y - (alpha*J1[1])
        J2 = np.array(grad(x,y))

        if(abs(np.dot(J1,J2))<=0.005):
            break
        count += 1
        mod_J = mod(J2)

    return x,y,count

start_points = np.array([2,1])

a = 0.05
b = 10

alpha = 0.05

x,y,iterations = steepest_gradient_descent(*start_points,a,b)

print("The minimum point found by steepest gradient method at fixed alpha is: ")
print(x,y)
print("")
print("The number of iterations is:")
print(iterations)
