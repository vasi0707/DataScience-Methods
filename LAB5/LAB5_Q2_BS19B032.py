#factorial function
def facto(n):
    if n==0:
        return 1
    if n>0:
        return n*facto(n-1)

n = int(input("Enter number to calculate factorial: "))
print("")
fact = facto(n)
print("Factorial using recursion")
print("The factorial of {} is: {}".format(n,fact))
print("")

print("Factorial using loops")
fact1 = 1
for i in range(2,n+1):
    fact1 = fact1*i
print("The factorial of {} is: {}".format(n,fact1))
print("")

#fibonacci series function
def fibo(num):
    if num==1:
        return 1
    if num==2:
        return 1
    else:
        return (fibo(num-1)+fibo(num-2))
    

num = int(input("Enter length of fibonacci series: "))

print("Fibonaci using recursion")
for i in range(1,num+1):
    print(fibo(i))
print("")

print("Fibonacci using loops")
first = 1
second = 1
if num==1:
    print(first)
elif num==2:
    print(first)
    print(second)
else:
    print(first)
    print(second)
    for i in range(2,num):
        print(first+second)
        first = second
        second = i

