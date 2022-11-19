#getting input number to check
check_num = int(input("Enter your number:"))

flag = 0

#checking whether any number less than half of given number divides it
for i in range(2,((check_num)//2)+1):
    if((check_num%i)==0):
        print("{} is not a prime".format(check_num))
        flag = 1
        break

if(flag==0):
    print("{} is a prime".format(check_num))
    
