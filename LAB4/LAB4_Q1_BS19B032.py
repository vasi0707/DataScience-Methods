#sports
sports = ['football','cricket','tennis']

#list of students
lst_stud = input("Enter list of students:").split()
print("")

like_lst = []

for student in lst_stud:
    print("Hi {}!".format(student))
    print("Which of these is your favourite sport: 1) {} 2) {} 3) {}".format(sports[0],sports[1],sports[2]))
    liked_sport = input("Enter here:")
    print("")
    like_lst.append(liked_sport)

#creating dictionary using dict comprehension
sport_dict = {k:v for k,v in zip(lst_stud,like_lst)}
print("The dictionary for favourite sport of students is:")
print(sport_dict)
