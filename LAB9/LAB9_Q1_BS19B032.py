import numpy as np
import matplotlib.pyplot as plt

def func(x,y):
    ans = (x-10)**2 + (y-10)**2
    return ans

def bracketing(a,b,n):
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

    return w1,w3

def interval_halving(A,B,n):
    a,b = bracketing(A,B,n)
    
    L = b-a

    while(abs(L)>0.005):
        wm = (a+b)/2
        x = start_points[0] + wm*direction[0]
        y = start_points[1] + wm*direction[1]
        Jm = func(x,y)
        w1 = a + (L/4)
        w2 = b - (L/4)
        x1 = start_points[0] + w1*direction[0]
        y1 = start_points[1] + w1*direction[1]
        x2 = start_points[0] + w2*direction[0]
        y2 = start_points[1] + w2*direction[1]
        J1 = func(x1,y1)
        J2 = func(x2,y2)
        if(J1<Jm):
            b = wm
            wm = w1
        elif(J2<Jm):
            a = wm
            wm = w2
        else:
            a = w1
            b = w2
        L = b-a

    return wm

start_points = np.array([2,1])
direction = np.array([2,5])

a = 0.05
b = 15
ans = interval_halving(a,b,100)

x1 = start_points[0] + ans*direction[0]
y1 = start_points[1] + ans*direction[1]

print("The value of alpha after minimisation is:")
print(ans)
print("")
print("The points were minimum lies in given direction and starting points is:")
print(x1,y1)

x = np.linspace(0,15,100)
y = np.linspace(0,15,100)
X,Y = np.meshgrid(x,y)
z = (X-10)**2 + (Y-10)**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('J(W1,W2)')
plt.show()

fig1 = plt.figure()
axes = fig1.gca()
axes.contour(X,Y,z)
axes.plot([start_points[0],direction[0]],[start_points[1],direction[1]])
axes.plot(x1,y1,'r',marker="o")
plt.show()


"""
As we can see from the contour plot that the minimising point(red point), does not lie in the initial line direction of points - (2,1) and (2,5).
Thus as we iterated, the alpha shifted towards the negative gradient.
So the search direction was a gradient descent one.
"""
