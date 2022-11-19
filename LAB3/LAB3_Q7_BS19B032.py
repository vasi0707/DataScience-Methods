#creating matrices

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[11,22,33],[44,55,66],[77,88,99]]
print(A)
print(B)
print("")

row_change = int(input("Enter a row to interchange:"))
col_change = int(input("Enter a column to interchange:"))

print("row interchanged")
if((row_change>=0) and (row_change<len(A))):
    row1 = [x for x in A]
    row2 = [y for y in B]
    temp = row1[row_change]
    row1[row_change] = row2[row_change]
    row2[row_change] = temp
    print(row1)
    print(row2)
else:
    print("wrong input - row")

print("")

print("column interchanged")
if((col_change>=0) and (col_change<len(A[0]))):
    At = zip(*A)
    Bt = zip(*B)
    col1 = [x for x in At]
    col2 = [y for y in Bt]
    temp = col1[col_change]
    col1[col_change] = col2[col_change]
    col2[col_change] = temp
    A2 = zip(*col1)
    B2 = zip(*col2)
    print(*A2)
    print(*B2)

else:
    print("wrong input - column")
