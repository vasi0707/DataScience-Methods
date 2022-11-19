#creating dictionaries

A = {'a':12,'b':32,'c':45,'d':19,'e':23}
B = {'e':77,'f':67,'b':99,'g':66,'l':12}

print("The two dictionaries are:")
print(A)
print(B)
print("")

C = A

for k,v in B.items():
    if k in C.keys():
        C[k] += B[k]
    else:
        C.update({k:v})

print("The final dictionary after adding is:")
print(C)
print("")

val_lst = C.values()
set1 = set(val_lst)

print("The set of unique values in dictionary are:")
print(set1)

