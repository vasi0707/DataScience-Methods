#minimum function

def mini(lst):
    if len(lst)==1:
        return lst[0]
    else:
        return min(lst[0],mini(lst[1:]))

#maximum function

def maxi(lst):
    if len(lst)==1:
        return lst[0]
    else:
        return max(lst[0],maxi(lst[1:]))

lst = [10,2,34,45,64,2,12,4,5,67,78,34]

print("Given list is:")
print(lst)
print("")
print("The minimum value in list is:")
print(mini(lst))
print("")
print("The maximum value in list is:")
print(maxi(lst))
