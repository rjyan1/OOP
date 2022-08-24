# Online Store OOP Practice
class Item:
    pay_rate = .70 # Pay rate after 30% Discount'
    all = []
    def __init__(self, name: str, price: float, quantity): #Initialize Method/Constructor
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
        
        # Actions to execute
        Item.all.append(self)
        
    def calculate_total_price(self, x, y): #Calcaulte Price Method
        return x * y
    
    def apply_discount(self): #Applying Discount Method
        self.price = self.price * self.pay_rate
    
    def __repr__(self): #Represent Object Method/Constructor
        return f"Item({self.name}, {self.price}, {self.quantity})"

# Instance Attributes
item1 = Item("Phone", 100, 5)
item2 = Item("DVI Tool", 4000, 4)
item3 = Item("Food", 300, 5)

# Class Attributes
print(Item.pay_rate)
print(item1.pay_rate)
print(item2.pay_rate)

print(Item.__dict__) #Lists all attributes from Item Class
print(item1.__dict__) #List all attributes from item1 instance

item1.apply_discount() # Pulls from the class level discount price
print(item1.price)


item2.pay_rate = .5 # Adjusting pay rate of item 2
item2.apply_discount()
print(item2.price) # Pulls from the instance level discount price

for instance in Item.all: #Prints all names of items in All List
    print(instance.name)
    
# __repr__ (Represents all objects)
print(Item.all)













