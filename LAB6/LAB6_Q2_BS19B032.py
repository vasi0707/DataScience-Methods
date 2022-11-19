import random

#function to print elements in matrix
def printmat(mat):
    for x in mat:  
        for ele in x:  
            print(ele, end = " ") 
        print("")

#Matrix Class
class Matrix:
    def __init__(self,m,n):
        self.row = m
        self.col = n
        self.mat = [[random.randint(1,10) for i in range(self.col)] for j in range(self.row)]
    def PrintMatrix(self):
        for x in self.mat:  
            for ele in x:  
                print(ele, end = " ") 
            print("")
    def __add__(self,other):
        mat1= [[val1+val2 for val1,val2 in zip(rowa,rowb)] for rowa,rowb in zip(self.mat,other.mat)]
        return mat1

    def __sub__(self,other):
        mat1= [[val1-val2 for val1,val2 in zip(rowa,rowb)] for rowa,rowb in zip(self.mat,other.mat)]
        return mat1
    def __mul__(self,other):
        mat1 = [[sum(val1*val2 for val1,val2 in zip(rowa,colb))for colb in zip(*other.mat)]for rowa in self.mat]
        return mat1
    def ElementMultiply(self,other):
        mat1= [[val1*val2 for val1,val2 in zip(rowa,rowb)] for rowa,rowb in zip(self.mat,other.mat)]
        return mat1
    def ScalarMultiplication(self,k):
        mat1 = []
        for i in self.mat:
            rows = list(map(lambda x:x*k,i))
            mat1.append(rows)
        return mat1

row1 = int(input("Enter number of rows for matrix1: "))
col1 = int(input("Enter number of columns for matrix1: "))
row2 = int(input("Enter number of rows for matrix2: "))
col2 = int(input("Enter number of columns for matrix2: "))
print("")

print("Matrix 1:")
mat1 = Matrix(row1,col1)
mat1.PrintMatrix()
print("")

print("Matrix 2:")
mat2 = Matrix(row2,col2)
mat2.PrintMatrix()
print("")

print("Addition of matrix")
if((row1==row2)and(col1==col2)):
    mat3 = mat1+mat2
    printmat(mat3)
else:
    print("Cannot Add")
print("")

print("Subtraction of matrix")
if((row1==row2)and(col1==col2)):
    mat4 = mat1-mat2
    printmat(mat4)
else:
    print("Cannot Subtract")
print("")

print("Multiplication of matrix")
if col1==row2:
    mat5 = mat1*mat2
    printmat(mat5)
else:
    print("Cannot Multiply")
print("")

print("Element wise multilication")
if((row1==row2)and(col1==col2)):
    mat6 = mat1.ElementMultiply(mat2)
    printmat(mat6)
else:
    print("Cannot multiply element wise")
print("")

scal = int(input("Enter scalar to multiply: "))
print("")
print("Scalar Multiplication with matrix 1")
mat7 = mat1.ScalarMultiplication(scal)
printmat(mat7)
print("")
print("Scalar Multiplication with matrix 2")
mat8 = mat2.ScalarMultiplication(scal)
printmat(mat8)
