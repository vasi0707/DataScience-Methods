#Student Class
class Student:
    def __init__(self,stud_name="",roll=""):
        self.student_name = stud_name
        self.roll_number = roll

    def get_details(self):
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        return name,roll

    def print_details(self):
        print("The name of student: ",self.student_name)
        print("The roll number is: ",self.roll_number)

#JEE Class
class JEE(Student):
    def __init__(self,stud_name="",roll="",phy=1,chem=1,math=1):
        super().__init__(stud_name,roll)
        self.physics_marks = phy
        self.chemistry_marks = chem
        self.maths_marks = math

    def get_marks(self):
        query = super().get_details()
        phy = int(input("Enter physics marks: "))
        chem = int(input("Enter chemistry marks: "))
        math = int(input("Enter maths marks: "))
        lst = [*query,phy,chem,math]
        return lst

    def print_details1(self):
        super().print_details()
        print("The physics marks are: ",self.physics_marks)
        print("The chemistry marks are: ",self.chemistry_marks)
        print("The maths marks are: ",self.maths_marks)

#Semester Class
class Semester(JEE):
    def __init__(self,name="",roll="",phy=1,chem=1,math=1,courses=[],cg=1.11):
        super().__init__(name,roll,phy,chem,math)
        self.courses = courses
        self.cgpa = cg

    def get_sem_details(self):
        query = super().get_marks()
        courses = input("Enter list of courses: ").split()
        cgp = float(input("Enter CGPA: "))
        lst = [*query,courses,cgp]
        return lst

    def print_details2(self):
        super().print_details1()
        print("The list of courses are: ")
        print(self.courses)
        print("The CGPA is: ",self.cgpa)
        
jee = JEE()
lst1 = jee.get_marks()
jee_obj = JEE(*lst1)
jee_obj.print_details1()
print("-------------")
sem = Semester()
lst2 = sem.get_sem_details()
sem_obj = Semester(*lst2)
sem_obj.print_details2()
