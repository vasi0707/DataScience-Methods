"""As tuple is immutable there is no tuple comprehension

But using list comprehension, later converting it into tuple

tuple comprehension can be done"""

#tuple comprehension for numbers 1 to 10

tup1 = tuple([x for x in range(1,11)])
print(tup1)
print("")

#tuple comprehension for even numbers from 1 to 10

tup2 = tuple([x for x in range(1,11) if x%2==0])
print(tup2)
print("")

#tuple comprehension to convert string to tuple

tup3 = tuple([x for x in "VASANTH"])
print(tup3)
