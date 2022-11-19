#sum function

def sums(lst):
    if len(lst)==1:
        return lst[0]
    else:
        mid_val = len(lst)//2
        return (sums(lst[0:mid_val])+sums(lst[mid_val:]))

#ascending function

def ascend(lst):
    if len(lst)<=1:
        return lst
    else:
        return ascend([x for x in lst[1:] if x<lst[0]])+ [lst[0]] + ascend([x for x in lst[1:] if x>=lst[0]])
        
        
    
lst = [1,2,4,45,6,23,4,5,7]
print("Given list is:")
print(lst)
print("")
ans = sums(lst)
print("The sum is:")
print(ans)
print("")
print("The sorted array is:")
print(ascend(lst))

