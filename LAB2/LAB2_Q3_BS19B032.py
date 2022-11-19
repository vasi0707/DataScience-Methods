#CONTINUE statement
#It skips the code for the particular iteration and continues for other iterations

str1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#using continue statement to print only consonants

for i in str1:
    if((i=="A") or (i=="E") or (i=="I") or (i=="O") or (i=="U")):
        continue
    else:
        print(i)

#PASS statement
#It is just a null statement to skip the code

#using pass statement to skip for loop

for i in str1:
    pass


