import math

check_num = int(input("Enter number to calculate:"))
terms = int(input("Enter the term upto which to calculate (give a large number for more accuracy):"))

#exp(x)
ex = 1

for i in range(1,(terms+1)):
    ex += ((check_num)**i)/(math.factorial(i))
print("exp({}) is {}".format(check_num,ex))

#sin x

sinx = 0
count = 0
for i in range(1,(terms+1),2):
    if(count%2==0):
        sinx = sinx + ((check_num)**i)/(math.factorial(i))
    else:
        sinx = sinx - ((check_num)**i)/(math.factorial(i))
    count += 1

print("sin({}) is {}".format(check_num,sinx))

#cos x

cosx = 1
count = 1
for i in range(2,(terms+1),2):
    if(count%2==0):
        cosx = cosx + ((check_num)**i)/(math.factorial(i))
    else:
        cosx = cosx - ((check_num)**i)/(math.factorial(i))
    count += 1

print("cos({}) is {}".format(check_num,cosx))
