#Class Containership

class Department:
    def __init__(self,deptname='BioTech'):
        self._deptname = deptname

    def print_dept(self):
        print("Printing in Department class")
        print(self._deptname)
        print("")
        
class Faculty:
    def __init__(self,deptname,fname='Ram',fid='1234'):
        self._fname = fname
        self._fid = fid
        self._dobj = Department(deptname)

    def print_faculty(self):
        print("Printing in Faculty class")
        print(self._fname, self._fid)
        self._dobj.print_dept()
        print("")

class Student:
    def __init__(self,deptname,studname="Vasi",roll="32"):
        self._deptname = Department(deptname)
        self._studname = studname
        self._rollno = roll

    def print_values(self):
        print("Printing in Student class")
        self._deptname.print_dept()
        print(self._studname,self._rollno)
        print("")

dept = Department()
fac = Faculty("BioTech")
stud = Student("BioTech")

print("Printing the values")
print("")
dept.print_dept()
print("")
fac.print_faculty()
print("")
stud.print_values()
