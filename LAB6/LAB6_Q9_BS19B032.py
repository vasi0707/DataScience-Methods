#Bill Class
class Bill:
    def __init__(self,cusname="",tabno=1,order=""):
        self.customer_name = cusname
        self.table_num = tabno
        self.order = order

    def getOrderDetails(self):
        name = input("Enter customer name: ")
        table_number = int(input("Enter table number: "))
        order = input("Enter orders: ")
        return name,table_number,order

    def TotalOrder(self):
        ord_lst = self.order.split(',')
        new_lst = []
        for i in ord_lst:
            new_lst.append(i.split('x'))
        orders = list(zip(*new_lst))
        return orders

#child class Restaurant Bill
class RestaurantBill(Bill):
    def __init__(self,name,tabno,order,order_lst,prices):
        super().__init__(name,tabno,order)
        self.order_lst = order_lst
        self.prices = prices

    def BillAmount(self):
        price_lst = self.prices.split(',')
        new_lst = []
        for i in price_lst:
            new_lst.append(i.split('-'))
        ord_price = list(zip(*new_lst))
        amount = 0
        for i in range(len(ord_price[0])):
            items1 = self.order_lst[0]
            items2 = ord_price[0]
            count = self.order_lst[1]
            price = ord_price[1]
            ind = items2.index(items1[i])
            amount += int(count[i])*int(price[ind])
        return amount

    def printBill(self,amount):
        print("Customer name: ",self.customer_name)
        print("Table no.: ",self.table_num)
        print("Total cost: ",amount)
        print("Taxes: ",12)
        print("Service Charges: ",8)
        print("Final Bill:")
        print(amount+12+8)      

bil = Bill()
lst = bil.getOrderDetails()
bill1 = Bill(*lst)
lst1 = bill1.TotalOrder()
print(lst1)
print("")
price = input("Enter the prices: ")
resbill = RestaurantBill(*lst,lst1,price)
final_bill = resbill.BillAmount()
resbill.printBill(final_bill)
