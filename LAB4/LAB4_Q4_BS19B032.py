#creating nested dictionary

nest_dct = {'bs19b032':{'name':'vasi','sem1_GPA':8.9,'sem2_GPA':8.9,'sem3_GPA':9,'CGPA':8.9},'bt19b001':{'name':'dev','sem1_GPA':9.1,'sem2_GPA':9.6,'sem3_GPA':9,'CGPA':9.2},'bt19b004':{'name':'sri','sem1_GPA':9.8,'sem2_GPA':9.5,'sem3_GPA':9,'CGPA':9.4},'bt19b036':{'name':'vino','sem1_GPA':8.5,'sem2_GPA':10.0,'sem3_GPA':9,'CGPA':9.1}}

print("The nested dictionary is:")
print(nest_dct)
print("")

def print_indi_items(dct):
    for k,v in dct.items():
        print(k,v)

def get_cgpa_list(dct):
    cg_list = []
    for roll,det in dct.items():
        for k,v in det.items():
            if k=="CGPA":
                cg_list.append(v)
    return cg_list

def sort_cgpa(dct,cg_lst):
    sort_dct = {}
    for cg in cg_lst:
        for roll,det in dct.items():
            for k,v in det.items():
                if k=="CGPA":
                    if v==cg:
                        sort_dct.update({roll:det})
    return sort_dct
    
print("The individual details are:")
print_indi_items(nest_dct)
print("")

cgpa_list = get_cgpa_list(nest_dct)
cgpa_list.sort()
sort_dct1 = sort_cgpa(nest_dct,cgpa_list)

print("The sorted dictionary as per CGPA is:")
print(sort_dct1)
print(" ")

print("The individual details of sorted dictionary are:")
print_indi_items(sort_dct1)
print(" ")

new_stud = {'bt19b010':{'name':'sakthi','sem1_GPA':8.0,'sem2_GPA':10.0,'sem3_GPA':9.0,'CGPA':9}}

print("The new student to be added is:")
print(new_stud)
print("")

sort_dct1.update(new_stud)
cgpa_list1 = get_cgpa_list(sort_dct1)
cgpa_list1.sort()
sort_dct2 = sort_cgpa(sort_dct1,cgpa_list1)

print("The sorted dictionary as per CGPA after adding is:")
print(sort_dct2)
print(" ")

print("The individual details of final sorted dictionary after adding are:")
print_indi_items(sort_dct2)
print(" ")

