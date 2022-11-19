#reversing function

def rev_str(str1,k):
    lst = str1.split()
    rev_lst = []
    for word in lst:
        new_str = word[::-1]
        rev_lst.append(new_str)
    if k=="words":
        return rev_lst
    else:
        return rev_lst[::-1]

#using recursion

def recur_rev(str1):
    if len(str1)==1:
        return str1
    else:
        return recur_rev(str1[1:]) + str1[0]

#print list as string

def str_print(lst):
    str1 = ""
    for i in lst:
        str1 = str1 + i
        str1 = str1 + " "
    return str1

line = input("Enter a sentence: ")
arg = input("Whether to revere words or sentence: ")
print("")
print("Reversing without recursion")
lst = rev_str(line,arg)
print(str_print(lst))
print("")

print("Using recursion")
lst1 = line.split()
reversed_lst = []
for word in lst1:
    reversed_lst.append(recur_rev(word))
if arg=="words":
    print(str_print(reversed_lst))
else:
    print(str_print(reversed_lst[::-1]))
