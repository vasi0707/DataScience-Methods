import csv

data = [['Students','Marks'],['vasi','95'],['dev','96'],['sri','97'],['vino','98'],['dvlv','99']]

with open('Q2_csv.txt','w') as csv_file:
    file1 = csv.writer(csv_file)
    for row in data:
        file1.writerow(row)

    
    
