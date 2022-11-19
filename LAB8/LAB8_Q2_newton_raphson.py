#Newton - Raphson method

def derv1(x):
    ans = 2*x - (54/x**2)
    return ans

def derv2(x):
    ans = 2 + (108/x**3)
    return ans

def newton_raphson(w,e):
    J1w = derv1(w)

    while(abs(J1w)>e):
        J1w = derv1(w)
        J2w = derv2(w)
        w = w - (J1w/J2w)
        J1w = derv1(w)

    return w

e = 0.04000000000000181    #bracketed value
w = 1

ans = newton_raphson(w,e)

print("The critical point is:")
print("w = ",ans)
