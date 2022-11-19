#string identifier
str1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#string slicing can take three arguments
#start, stop, step

#step 2
print("String slicing with start=0, stop=26, step=2")
print(str1[0:26:2])
print("")
#step5
print("String slicing with start=10, stop=25, step=5")
print(str1[10:25:5])
print("")

#For string reversing we can use a step of -1
print("The reversed string of /'{}/' is".format(str1))
print(str1[-1:-27:-1])
