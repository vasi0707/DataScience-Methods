import random

#Complex Class
class Complex:
    def __init__(self,r=1,i=1):
        self.real = r
        self.imaginary = i
    def PrintComplex(self):
        if self.imaginary>=0:
            str1 = str(self.real)+"+"+str(self.imaginary)+"i"
            print(str1)
        else:
            str1 = str(self.real)+str(self.imaginary)+"i"
            print(str1)

#Derived Class 1
class Derived1(Complex):
    def __init__(self,r,i):
        super().__init__(r,i)
    def Print(self1):
        super().PrintComplex()
    def conjugate(self):
        C = Complex()
        C.real = self.real
        C.imaginary = -1*self.imaginary
        return C

comp1 = Derived1(3,4)
comp1.Print()
comp2 = comp1.conjugate()
comp2.PrintComplex()
print("----------")

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
#Derived Class
class Derived2(Matrix):
    def __init__(self,m,n):
        super().__init__(m,n)
    def Print(self):
        super().PrintMatrix()
    def ScalarMultiplication(self,k):
        mat1 = []
        for i in self.mat:
            rows = list(map(lambda x:x*k,i))
            mat1.append(rows)
        return mat1

mat1 = Derived2(3,4)
mat1.Print()
print("----------")
mat2 = mat1.ScalarMultiplication(3)
for x in mat2:  
    for ele in x:  
        print(ele, end = " ") 
    print("")
