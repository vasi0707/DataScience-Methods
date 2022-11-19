#Variable Member Functions for strings

str1 = "Apple"
str2 = "This is the first lab"
check_str = "apple ball cat/dog/eagle/ fish//goat//hen// A/B//C"

#split function
#split a string into a list
print("Split at space")
print(check_str.split())    #split at space
print("")
print("Split at /")
print(check_str.split('/')) #split at /
print("")
print("Split at //")
print(check_str.split('//'))    #split at //
print("")

#partition function
#split string into tuple at specified string
print("Partition at dog")
print(check_str.partition("dog"))
print("")

#find function
#find the position of specified string
print("The position of l in Apple is:")
print(str1.find("l"))
print("")

#replace function
#replace specified string
print("Replacing first with second in str2")
print(str2.replace("first","second"))
print("")

#upper function
#converts all characters to upper case
print("Converting Apple to upper case:")
print(str1.upper())
print("")

#lower function
#converts all characters to lower case
print("Converting Apple to lower case:")
print(str1.lower())
print("")

#isupper function
#checks whether all characters are upper case
print("Checking whether Apple is upper case:")
print(str1.isupper())
print("")

#islower function
#checks whether all characters are lower case
print("Checking whether Apple is lower case:")
print(str1.islower())
print("")

#isalnum function
#checks whether all characters are alphabets or numbers
print("Checking whether Apple is alphanumeric:")
print(str1.isalnum())
print("")
