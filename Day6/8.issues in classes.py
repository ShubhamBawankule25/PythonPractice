

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        # self.price = max(price, 0)
        if price > 0:               # code will not accept negative price
            self.price = price
        else:
            self.price = 0
        # self.allSpecs = f"{self.brand} {self.model} and price is Rs {self.price}"
    
    @property       #with this method behaves like attribute
    def allSpecs(self):
        return f"{self.brand} {self.model} and price is Rs {self.price}"
    
    def fullname(self):
        return f"{self.brand}  {self.model}"
    
phone1 = Phone("Nokia", "6", -15000)


print(phone1.fullname())

print(phone1.allSpecs()) #<-- without @property
print(phone1.allSpecs)  #<--- with @property
