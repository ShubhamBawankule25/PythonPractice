class Laptop:
    discount = 10   #<--- class variable every object will use untill it has a discount attribute specified
    sno = 0 #<---- adding serial number to every object
    def __init__(self, name, price):
        Laptop.sno += 1
        self.sno = Laptop.sno   # incrementing serial number by 1 with every object creation
        self.name = name
        self.price = price
        
        
    def discountedPrice(self):
        # disc_amt = (self.discount/100) * self.price <--- if we use this only class variable 10% will be used
        disc_amt = (self.discount/100) * self.price
        finalAmt = self.price - disc_amt
        return round(finalAmt,3)
        
l1 = Laptop("Macbook Pro 16inch", 200000)
l1.discount = 20  # <----- giving specific discount attribute to l1 
# O/P {'name': 'Macbook Pro 16inch', 'price': 200000, 'discount': 20, 'bluetooth': 'Yes'}

l1.bluetooth = "Yes" #<----- we can append attributs to objects in this way

print(l1.__dict__)
print(l1.discountedPrice()) # l1 will use 20% as specified

l2 = Laptop("Acer Nitro 5", 70000)
print(l2.__dict__)
print(l2.discountedPrice())  # l2 will use 10% from class variable

l3= Laptop("HP Probook", 70000)
l3.discount = 0
print(l3.__dict__)
print(l3.discountedPrice())