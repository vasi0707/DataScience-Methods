import random

#taking input for length of list
length = int(input("Enter the length of list:"))

lst = []

#creating list with random integers from 1 to 100
for i in range(length):
    lst.append(random.randrange(1,100))

print("The initial list is:")
print(lst)
print("")

lst.sort()

print("The sorted list is:")
print(lst)
print("")

median_index = 0
median = 0

#finding median index and median
if(length%2==0):
    median_index = int(length/2)
    median = (lst[median_index-1] + lst[median_index])/2

else:
    median_index = int((length+1)/2)
    median = lst[median_index-1]

sublist1 = lst[0:median_index]
sublist2 = lst[median_index:]

print("The median is:",median)
print("")
print("The first sublist is:")
print(sublist1)
print("")
print("The second sublist is:")
print(sublist2)
print("")
