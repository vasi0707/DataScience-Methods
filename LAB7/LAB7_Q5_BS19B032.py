#csv reader in pandas

import pandas as pd

file = pd.read_csv('Q5.csv')

print("Printing list of students")
print(file['students'])
print("")

print("Printing list of marks")
print(file['marks'])
print("")

print("Printing entire data")
print(file)
