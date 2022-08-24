class Item:
    def __init__(self, name: str, price: float, quantity):
        # Run Validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        
        # Assign to self object
        print(f"An instance created: {name}")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.calculate = quantity * price
        print("The total price for", self.name, "is:", self.calculate)
        
    def calculate_total_price(self, x, y):
        return x * y


item1 = Item("Phone", 100, 5)
item2 = Item("DVI Tool", 4000, 4)












