#getting list of food items

food_list = input("Enter the food list:").split()
food_list.sort()
food_dct = {}

food_num = 0
while(food_num<len(food_list)):
    food = food_list[food_num]
    orders = food_list.count(food)
    food_dct.update({food:orders})
    food_num += orders

sort_food = sorted(food_dct)
final_food_dct = {}

for i in sort_food:
    order = food_dct[i]
    final_food_dct.update({i:order})

print("")
print("The final sorted food order dictionary is:")
print(final_food_dct)
print("")

max_food = ""
max_order = 0

for k,v in final_food_dct.items():
    if v>max_order:
        max_order = v
        max_food = k

print("The maximum ordered food was:")
print(max_food)
    
