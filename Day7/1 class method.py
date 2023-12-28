class Laptop:
    discount = 10   
    sno = 0 #<---- adding serial number to every object
    def __init__(self, name, price):
        Laptop.sno += 1
        self.sno = Laptop.sno   # incrementing serial number by 1 with every object creation
        self.name = name
        self.price = price
        
    @classmethod
        
    def discountedPrice(self):
        # disc_amt = (self.discount/100) * self.price <--- if we use this only class variable 10% will be used
        disc_amt = (self.discount/100) * self.price
        finalAmt = self.price - disc_amt
        return round(finalAmt,3)