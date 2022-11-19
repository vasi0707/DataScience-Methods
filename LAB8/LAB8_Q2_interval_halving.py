#Interval Halving

def func(x):
    ans = x**2 + (54/x)
    return ans

def interval_halving(a,b,e):
    L = b-a

    while(abs(L)>e):
        wm = (a+b)/2
        Jm = func(wm)
        w1 = a + (L/4)
        w2 = b - (L/4)
        J1 = func(w1)
        J2 = func(w2)
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

e = 0.04000000000000181    #bracketed value
a = 1
b = 7

ans = interval_halving(a,b,e)

print("The critical point is:")
print("w = ",ans)
