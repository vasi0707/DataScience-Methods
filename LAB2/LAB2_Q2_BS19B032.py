#getting input from user
a = int(input("Enter your first number:"))
b = int(input("Enter your second number:"))
c = int(input("Enter your thrird number:"))
print("")

#approach 1
if a>b:
    if a>c:
        print("By approach 1, {} is largest".format(a))
    else:
        print("By approach 1, {} is largest".format(c))
else:
    if b>c:
        print("By approach 1, {} is largest".format(b))
    else:
        print("By approach 1, {} is largest".format(c))

print("")

#approach 2
if((a>b) and (a>c)):
    print("By approach 2, {} is largest".format(a))
elif((b>a) and (b>c)):
    print("By approach 2, {} is largest".format(b))
else:
    print("By approach 2, {} is largest".format(c))

print("")

#approach 3
if((a>b>c) or (a>c>b)):
    print("By approach 3, {} is largest".format(a))
if((b>c>a) or (b>a>c)):
    print("By approach 3, {} is largest".format(b))
if((c>b>a) or (c>a>b)):
    print("By approach 3, {} is largest".format(c))

print("")

#conditional expression two lines
maxi1 = 0
maxi1 = a if a>b else b
maxi1 = c if c>maxi1 else maxi1

print("By conditional expression in two lines, the largest number is:",maxi1)
print("")

#one line conditional expression
maxi2 = 0
maxi2 = a if (a>b) and (a>c) else ( b if (b>a) and (b>c) else c )

print("By one line conditional expression, the largest number is:",maxi2)

