import math

#integer identifiers
a = 2
b = 3
c = -4
d = 1.5
e = -2.8

#absolute function
print("The absolute value of {} is:".format(a))    #returns the absolute value of the number
print(abs(a))
print("The absolute value of {} is:".format(c))
print(abs(c))

print("")

#power function
print("{} power {} is:".format(a,b))    #returns the power of given number to another number
print(pow(a,b))
print("{} power {} is:".format(c,b))
print(pow(c,b))

print("")

#square root function
print("The square root of {} is:".format(a))    #returns square root of given number 
print(math.sqrt(a))
print("The square root of {} is:".format(b))
print(math.sqrt(b))

print("")

#factorial function
print("The factorial of {} is:".format(a))  #returns factorial of given number
print(math.factorial(a))
print("The factorial of {} is:".format(b))
print(math.factorial(b))

print("")

#rounding functions
#ceil function - rounds a number up to the nearest integer
print("The round up of {} is:".format(d))
print(math.ceil(d))
print("The round up of {} is:".format(e))
print(math.ceil(e))

print("")

#floor function - rounds a number down to the nearest integer
print("The round down of {} is:".format(d))
print(math.floor(d))
print("The round down of {} is:".format(e))
print(math.floor(e))

print("")
