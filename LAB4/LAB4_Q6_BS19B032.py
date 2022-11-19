#given sets

Metro_Cities = {'Mumbai', 'Chennai', 'New Delhi', 'Pune', 'Bangalore', 'Hyderabad'}
Coastal_Cities = {'Surat', 'Vizag', 'Chennai', 'Panaji', 'Mumbai', 'Cochin'}

print("Given sets are:")
print("Set - Metro Cities")
print(Metro_Cities)
print("Set - Coastal Cities")
print(Coastal_Cities)
print("")

print("The Metro cities which are also Coastal are:")
both_set = Metro_Cities & Coastal_Cities 
print(both_set)
print("")

union_set1 = Metro_Cities - Coastal_Cities
union_set2 = Coastal_Cities - Metro_Cities

final_set = union_set1 | union_set2

print("Cities that are either Metropolitan or Coastal but not both are:")
print(final_set)
