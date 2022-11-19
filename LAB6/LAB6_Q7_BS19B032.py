#Different Classes
class Department:
    def __init__(self,deptname='BioTech'):
        self.deptname = deptname

    def print_dept(self):
        print(self.deptname)
        
class Faculty:
    def __init__(self,deptname,fname='Ram',fid='1234'):
        self.fname = fname
        self.fid = fid
        self.deptname = deptname

    def print_faculty(self):
        print(self.fname, self.fid)

class Student:
    def __init__(self,deptname,studname="Vasi",roll="32"):
        self.deptname = deptname
        self.stuname = studname
        self.rollno = roll

    def print_values(self):
        print(self.stuname,self.rollno)

#Multiple Inherited Class
class Inherit(Department,Faculty,Student):
    def __init__(self,deptname,facname,facid,studname,roll):
        Department.__init__(self,deptname)
        Faculty.__init__(self,deptname,facname,facid)
        Student.__init__(self,deptname,studname,roll)
    def print_det(self):
        Department.print_dept(self)
        Faculty.print_faculty(self)
        Student.print_values(self)

inherit1 = Inherit("EngDesign","Ram","1","Vino","33")
inherit1.print_det()
print("")
inherit2 = Inherit("EngDesign","Joy","2","Dev","12")
inherit2.print_det()
print("")
inherit3 = Inherit("Biotech","Chand","3","Vasi","32")
inherit3.print_det()
print("")
inherit4 = Inherit("Biotech","Chand","3","Sri","18")
inherit4.print_det()
