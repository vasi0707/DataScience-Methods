#map function
#This function maps a given function to the list of values provided

def square(n):
    return n*n

lst = [1,2,3,4,5]
print("Map function:")
print(*map(square,lst))
print("")

#filter function
#This function filters out values in a given list

lst1 = ['a','b','c','d','e','f','g','h','i']
vowel_lst = ['a','e','i','o','u']

print("Filter function")
print(*filter(lambda x: x in vowel_lst,lst1))
print("")

#reduce function
#This function helps to apply a particular function to list in pairs
import functools

print("Reduce function")
lst2 = [1,2,3,4,5,6,7,8]
print(functools.reduce(lambda x,y: x+y,lst2))



