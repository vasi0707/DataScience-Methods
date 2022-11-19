import numpy as np

def pascals_triangle(n):
    line_1=[1]      #initialising first line as array    

    preceding_line=line_1

    if(n==1):
        line=line_1    

    for i in range(2,n+1):
        line=np.empty(i,dtype=int)    #initialising empty array for each line
        for j in range(i):
            if(j==0):
                line[j]=1
            elif(j==(i-1)):        #assigning first and last element of array as 1
                line[j]=1
            else:
                line[j]=preceding_line[j]+preceding_line[j-1]    #finding the element of given line using preceding line
        preceding_line=line    #assigning current line as preceding line for next line

    return line

#getting input from user
n = int(input("Enter number of rows:"))
print("")

for i in range(1,n+1):
    a=pascals_triangle(i)    #printing all lines from 1 to n 
    for j in range(i):
        print(a[j]," ",end='')
    print(end='\n')
