#importing random library
import random

#creating a list using list comprehension and random number generation
lst = [random.randint(10,100) for i in range(20)]
print("The created list is:")
print(lst)
print("")

#printing even numbers
print("The even numbers are:")
lst1 = [print(x) for x in lst if x%2==0]
print("")

#printing odd numbers
print("The odd numbers are:")
lst1 = [print(x) for x in lst if x%2==1]
print("")

#printing numbers divisible by 3
print("The numbers divisible by 3 are:")
lst1 = [print(x) for x in lst if x%3==0]
print("")


