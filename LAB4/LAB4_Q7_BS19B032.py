#function to check anagrams

def check_anagram(lst):
    dct = {}
    str1 = lst[0]
    for i in str1:
        if i not in dct.keys():
            occur = str1.count(i)
            dct.update({i:occur})
    for i in range(1,len(lst)):
        str2 = lst[i]
        flag = 0
        if len(str2)==len(str1):
            for j in str2:
                if j in dct.keys():
                    occur = str2.count(j)
                    if occur==dct[j]:
                        continue
                    else:
                        flag = 1
                        break
                else:
                    flag = 1
                    break
        else:
            flag = 1
            break
    if flag==0:
        return "TRUE"
    else:
        return "FALSE"

#getting list

lst1 = input("Enter the list:").split()
print("")
print(check_anagram(lst1))

