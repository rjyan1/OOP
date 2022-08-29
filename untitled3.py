# When to use class methods and when to use static methods
import csv
class Item:
    pay_rate = .70 # Pay rate after 30% Discount'
    all = []
    
    def __init__(self, name, price, quantity): #Initialize Method/Constructor
        # Run Validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        self.calculate = quantity * price
        print(f"An instance created: {name}")
        print("The total price for", self.name, "is:", self.calculate)
        
        # Actions to execute
        Item.all.append(self)
    
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        
        # Static methods should do something that has
        # a relationship with the class, but not
        # something that must be unique per instance!
    
    
    @classmethod # Decorator to instantiate class method
    def instantiate_from_csv(cls): #Instantiating Class Method
        with open('Data.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = str(item.get('name')),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
                )
            
        # This should do something that has a 
        # relationship with the class
        # but usually, those are used to manipulate 
        # different structures of data to instantiate
        # objects, like we have done with CSV
    
    # MAIN DIFFERENCE: Static methods are not passing
    # the object reference as the first argument
    
class Phone(Item):
    # This Super function takes all of the attributes AND methods of the parent class.
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(
            name, price, quantity
            
            )
    
    

phone1 = Phone("version1", 500, 5)
phone1.broken_phones = 1
phone2 = Phone("version2", 700 ,5)
phone2.broken_phones = 2

