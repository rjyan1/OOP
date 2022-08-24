class Item:
    def calculate_total_price(self, x, y):
        return x * y


item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price , item1.quantity))

item2 = Item()
item2.name = "DVI Tool"
item2.price = 4000
item2.quantity = 4
print('The total price is $',item2.calculate_total_price(item2.price,item2.quantity))




