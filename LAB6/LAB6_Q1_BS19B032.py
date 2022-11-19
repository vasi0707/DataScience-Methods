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
    def AddComplex(self,other):
        C = Complex()
        C.real = self.real + other.real
        C.imaginary = self.imaginary + other.imaginary
        return C
    def __add__(self,other):
        C = Complex()
        C.real = self.real + other.real
        C.imaginary = self.imaginary + other.imaginary
        return C
    def SubtractComplex(self,other):
        C = Complex()
        C.real = self.real - other.real
        C.imaginary = self.imaginary - other.imaginary
        return C
    def __sub__(self,other):
        C = Complex()
        C.real = self.real - other.real
        C.imaginary = self.imaginary - other.imaginary
        return C
    def MultiplyComplex(self,other):
        C = Complex()
        C.real = (self.real*other.real)-(self.imaginary*other.imaginary)
        C.imaginary = (self.real*other.imaginary) + (self.imaginary*other.real)
        return C
    def __mul__(self,other):
        C = Complex()
        C.real = (self.real*other.real)-(self.imaginary*other.imaginary)
        C.imaginary = (self.real*other.imaginary) + (self.imaginary*other.real)
        return C
    def DivideComplex(self,other):
        C = Complex()
        C.real = ((self.real*other.real)+(self.imaginary*other.imaginary))/(other.imaginary**2+other.real**2)
        C.imaginary = ((self.imaginary*other.real)-(self.real*other.imaginary))/(other.imaginary**2+other.real**2)
        return C
    def __truediv__(self,other):
        C = Complex()
        C.real = ((self.real*other.real)+(self.imaginary*other.imaginary))/(other.imaginary**2+other.real**2)
        C.imaginary = ((self.imaginary*other.real)-(self.real*other.imaginary))/(other.imaginary**2+other.real**2)
        return C
    def FloorDivideComplex(self,other):
        C = Complex()
        C.real = ((self.real*other.real)+(self.imaginary*other.imaginary))//(other.imaginary**2+other.real**2)
        C.imaginary = ((self.imaginary*other.real)-(self.real*other.imaginary))//(other.imaginary**2+other.real**2)
        return C
    def __floordiv__(self,other):
        C = Complex()
        C.real = ((self.real*other.real)+(self.imaginary*other.imaginary))//(other.imaginary**2+other.real**2)
        C.imaginary = ((self.imaginary*other.real)-(self.real*other.imaginary))//(other.imaginary**2+other.real**2)
        return C

print("Printing Given Complex Numbers")
comp1 = Complex(2,3)
comp1.PrintComplex()
comp2 = Complex(9,10)
comp2.PrintComplex()
print("")
print("Addition of complex numbers")
comp3 = comp1.AddComplex(comp2)
comp3.PrintComplex()
comp4 = comp1 + comp2
comp4.PrintComplex()
print("")
print("Subtraction of complex numbers")
comp5 = comp2.SubtractComplex(comp1)
comp5.PrintComplex()
comp6 = comp2 - comp1
comp6.PrintComplex()
print("")
print("Multiplication of complex numbers")
comp7 = comp1.MultiplyComplex(comp2)
comp7.PrintComplex()
comp8 = comp1*comp2
comp8.PrintComplex()
print("")
print("Ture division of complex numbers")
comp9 = comp2.DivideComplex(comp1)
comp9.PrintComplex()
comp10 = comp2/comp1
comp10.PrintComplex()
print("")
print("Floor division of complex numbers")
comp11 = comp2.FloorDivideComplex(comp1)
comp11.PrintComplex()
comp12 = comp2//comp1
comp12.PrintComplex()
