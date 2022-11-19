#creating tuples
name = ('vasi','dev','james','alice','lopez')
age = (20,21,34,19,56)
salary = (50000,60000,100000,20000,150000)

#grouping using indexing

tup1 = tuple([(name[i],age[i],salary[i]) for i in range(len(name))])
print(tup1)

#grouping using zip function

tup2 = zip(name,age,salary)
print(*tup2)

