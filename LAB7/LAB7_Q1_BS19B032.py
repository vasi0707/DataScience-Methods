#creating a csv file

file = open("marks.txt",'w')
file.write("Student,Marks \n")
for i in range(5):
    student_name = input("Enter student name: ")
    marks = input("Enter student's mark: ")
    file.write(student_name)
    file.write(",")
    file.write(marks)
    file.write("\n")

file.close()
