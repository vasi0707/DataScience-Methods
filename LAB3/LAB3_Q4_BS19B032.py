#creating tuple and list

lst = [1,2,3,"vasi","123",[55,66,77]]
tup = (1,2,3,"vasi","123",(55,66,77))

#changing elements of list

lst[1] = 999
print(lst)
print("")

"""This is not possible"""
#tup[1] = 999

#appending elements to list

lst.append(79)
print(lst)
print("")

"""This is not possible"""
#tup.append(79)

#removing elements from list

lst.remove(1)
print(lst)
print("")

"""This is not possible"""
#tup.remove(1)

#popping

lst.pop()
print(lst)
print()

"""This is not possible"""
#tup.pop()

