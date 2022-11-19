#creating a list of bank_accounts
bank_account = [["ravi",101,"07-08-99","chennai",1000],["krat",102,"08-09-96","salem",10000],["yout",103,"1-9-89","kovai",5000],["yout",103,"1-9-89","kovai",5000]]

print("The account details are:")
print(bank_account)
print("")

#taking query to add
query1 = input("Enter a bank detail to add:").split()
query_name1 = query1[0]
pos1 = 0
pos1 = int(pos1)

#adding query alphabeticaly
for i in range(len(bank_account)):
    detail = bank_account[i]
    name = detail[0]
    letter1 = name[0]
    if(ord(query_name1[0])>ord(letter1)):
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
pos2 = 0
pos2 = int(pos2)

for i in range(len(bank_account)):
    detail = bank_account[i]
    name1 = detail[0]
    if(name1==query2):
        pos2 = i
        break
bank_account.remove(bank_account[pos2])
print("The updated bank account after deleting is:")
print(bank_account)
print("")

query3 = input("Enter a bank detail to add at begining:").split()

#taking input to add at start
bank_account.insert(0,query3)
print("The updated bank account after adding is:")
print(bank_account)
print("")

#removing the duplicates
length = len(bank_account)
i=0
while(i<length):
    detail2 = bank_account[i]
    name2 = detail2[0]
    count = i+1
    for j in range(count,length):
        chk = bank_account[j]
        nme = chk[0]
        if(nme==name2):
            bank_account.remove(bank_account[j])
            length = length-1
    i+=1

print("The updated bank account after removing duplicates is:")
print(bank_account)
print("")

names = []
for i in range(len(bank_account)):
    detail3 = bank_account[i]
    names.append(detail3[0])
names.sort()

final_bank_account = []

for j in range(len(names)):
    chk = names[j]
    for i in range(len(bank_account)):
        detail4 = bank_account[i]
        name4 = detail4[0]
        if(chk==name4):
            final_bank_account.append(detail4)
            break
        
print("The final updated bank account:")
print(final_bank_account)
print("")
