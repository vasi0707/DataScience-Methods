#Bracketing Method

#Given Function
#J(w) = w^2 + (54/w)

def func(x):
    ans = x**2 + (54/x)
    return ans


def bracketing(a,b,n):
    del_w = (b-a)/n
    w1 = a
    w2 = a + del_w
    w3 = w2 + del_w

    flag = 0

    while w3<=b:
        J1 = func(w1)
        J2 = func(w2)
        J3 = func(w3)
        if((J1>=J2) and (J2<=J3)):
            flag = 1
            break
        else:
            w1 = w2
            w2 = w3
            w3 = w3 + del_w

    if flag==0:
        Ja = func(a)
        Jb = func(b)
        if Ja<Jb:
            w2 = a
        else:
            w2 = b

    return w2

a=1
b=7
n=50

ans = bracketing(a,b,n)

print("The critical point is:")
print("w = ",ans)
