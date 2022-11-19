#Taking the input
query = input("Enter integer or string:")

#creating a list
lst = list(query)

sums = 0

for i in range(len(lst)):
    if(ord(lst[i])>58):
        sums += ord(lst[i]) #finding sum of ASCII code if query is string
    else:
        sums += int(lst[i])   #finding sum of digits if query is integer

print("The sum is:",sums)


