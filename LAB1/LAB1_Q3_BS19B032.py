import random

random.seed(10)
a=random.randrange(1,10)
b=random.randrange(1,10)
c=random.randrange(1,10)
d=random.randrange(1,10)
e=random.randrange(1,10)

#operators
print("Addition:{},{}".format(a,b))
print(a+b)
print("Subtraction:{},{}".format(c,d))
print(c-d)
print("Multiplication:{},{}".format(a,c))
print(a*c)
print("Division:{},{}".format(b,d))
print(b/d)
print("Modulus:{},{}".format(e,d))
print(e%d)
print("Floor Division:{},{}".format(b,e))
print(b//e)
print("Exponent:{},{}".format(b,c))
print(b**c)
