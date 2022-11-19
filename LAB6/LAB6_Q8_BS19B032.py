#Father Class
class Father:
    def __init__(self,name="",age=1,talent=[]):
        self.father_name = name
        self.father_age = age
        self.father_talents = talent

#Mother Class
class Mother:
    def __init__(self,name1="",age1=1,talent1=[]):
        self.mother_name = name1
        self.mother_age = age1
        self.mother_talents = talent1

#Child Class
class Child(Father,Mother):
    def __init__(self,name="",age=1,talent=[],name1="",age1=1,talent1=[],name2="",age2=1,gender=""):
        Father.__init__(self,name,age,talent)
        Mother.__init__(self,name1,age1,talent1)
        self.child_name = name2
        self.child_age = age2
        self.child_gender = gender

    def getChildDetails(self):
        name = input("Enter Father name: ")
        age = int(input("Enter Father age: "))
        talent = input("Enter Father talents: ").split()
        name1 = input("Enter Mother name: ")
        age1 = int(input("Enter Mother age: "))
        talent1 = input("Enter Mother talents: ").split()
        name2 = input("Enter Child name: ")
        age2 = int(input("Enter Child age: "))
        gender = input("Enter Child gender: ")
        father1 = [name,age,talent]
        mother1 = [name1,age1,talent1]
        child1 = [name2,age2,gender]
        return father1,mother1,child1

    def printChildDetails(self):
        print("Father name: ",self.father_name)
        print("Father age: ",self.father_age)
        print("Father talents: ",self.father_talents)
        print("Mother name: ",self.mother_name)
        print("Mother age: ",self.mother_age)
        print("Mother talents: ",self.mother_talents)
        print("Child name: ",self.child_name)
        print("Child age: ",self.child_age)
        print("Child gender: ",self.child_gender)

    def displayTalents(self):
        chi_tal = set(self.father_talents) & set(self.mother_talents)
        print("Child talents are: ")
        print(chi_tal)

child1 = Child()
inherit = child1.getChildDetails()
father_details = inherit[0]
mother_details = inherit[1]
child_details = inherit[2]
father1 = Father(*father_details)
mother1 = Mother(*mother_details)
child2 = Child(*father_details,*mother_details,*child_details)
print("--------------")
child2.printChildDetails()
child2.displayTalents()
