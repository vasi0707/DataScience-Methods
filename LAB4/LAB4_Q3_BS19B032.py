#getting input string

str1 = input("Enter your string:")
print("")

dct = {}

for i in str1:
    if i not in dct.keys():
        occur = str1.count(i)
        dct.update({i:occur})

print("The dictionary for occurance of letters in string is:")
print(dct)
print("")

for letter in str1:
    if dct[letter]==1:
        print("First occuring unique letter is: {}".format(letter))
        break
print("")

new_str1 = ""
for lett in str1:
    if lett not in new_str1:
        new_str1 += lett

print("The new string without duplicates:")
print(new_str1)
print("")

set1 = set(str1)
new_str2 = ""

for let in str1:
    if let in set1:
        new_str2 += let
        set1.remove(let)

print("The new string without duplicates using set is:")
print(new_str2)
