#creating a list of bank_accounts
bank_account = ["ravi","krat","yout","frie","anud","mnd","yout","yout"]
bank_account.sort()

print("The account details are:")
print(bank_account)
print("")

#taking query to add
query1 = input("Enter a bank detail to add:")
pos1 = 0
pos1 = int(pos1)

#adding query alphabeticaly
for i in range(len(bank_account)):
    name = bank_account[i]
    letter1 = name[0]
    if(ord(query1[0])>ord(letter1)):
        continue
    else:
        pos1 = i
        break

bank_account.insert(pos1,query1)
print("The updated bank account after inserting is:")
print(bank_account)
print("")

#taking query to remove
query2 = input("Enter a bank detail to remove:")

bank_account.remove(query2)
print("The updated bank account after deleting is:")
print(bank_account)
print("")

query3 = input("Enter a bank detail to add at begining:")

#taking input to add at start
bank_account.insert(0,query3)
print("The updated bank account after adding is:")
print(bank_account)
print("")

#removing the duplicates
for name in bank_account:
    count = bank_account.count(name)
    if count>1:
        for i in range(count-1):
            bank_account.remove(name)

print("The updated bank account after removing duplicates is:")
print(bank_account)
print("")

bank_account.sort()

print("The final updated bank account:")
print(bank_account)
print("")
