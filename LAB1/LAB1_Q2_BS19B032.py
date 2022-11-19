from tabulate import tabulate

data = [['Parentheses','()','Left to Right'],
['Exponent','**','Left to Right'],
['Unary Operations','+a,-a','Left to Right'],
['Multiplication,Division,Modulus,Floor Division','*,/,%,//','Left to Right'],
['Addition,Subtraction','+,-','Left to Right'],
['Assignment Operators','=','Right to Left'],
['Comparison Operators','==,!=,<,>','Right to Left']]

print (tabulate(data, headers=["Operations", "Operator", "Direction"]))

print("")
a = 2**3/8+(7*2//6)-9
print("The value of expression 2**3/8+(7*2//6)-9 is:")
print(a)
