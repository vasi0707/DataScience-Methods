#getting order details

file1 = open("order_list.txt",'r')
orders = file1.readlines()
file1.close()

file2 = open("price_list.txt",'r')
prices = file2.readlines()
file2.close()

order_details = []
items = []
price = []

for row1 in orders:
    det1 = row1.split(':')
    order_details.append(det1)

order = order_details[2:]

for row2 in prices:
    det2 = row2.split(':')
    items.append(det2[0])
    price.append(det2[1])

bill = 0

for i in order:
    order_name = i[0]
    order_count = int(i[1])
    ind = items.index(order_name)
    bill += order_count*(int(price[ind]))

file3 = open("bill.txt",'w')
file3.write(order_details[0][0])
file3.write(": ")
file3.write(order_details[0][1])
file3.write(order_details[1][0])
file3.write(": ")
file3.write(order_details[1][1])
file3.write("Total Amount")
file3.write(": ")
file3.write(str(bill))
file3.close()
