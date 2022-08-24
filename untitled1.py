class Item:
    def __init__(self, name:str, price:float, quantity):
        # Run Validations to the received arguments
        assert price >= 0
        assert quantity >= 0
        
        # Assign to self object
        print(f"An instance created: {name}")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.calculate = quantity * price
    def calculate_total_price(self, x, y):
        return x * y


item1 = Item("Phone", -100, 5)


item2 = Item("DVI Tool", 4000, 4)

print(item1.name)
print(item2.name)
print(item1.price)
print(item2.price)
print(item1.quantity)
print(item2.quantity)
print(item1.calculate)










