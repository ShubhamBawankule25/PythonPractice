class Laptop:
    discount = 10   
    sno = 0 #<---- adding serial number to every object
    def __init__(self, name, price):
        Laptop.sno += 1
        self.sno = Laptop.sno   # incrementing serial number by 1 with every object creation
        self.name = name
        self.price = price
        
        
    # both classmethod and stratic methods are rarely used to save memory 
    # used to improve readability of code
    
    
    @classmethod
    def from_string(clr,string):  
    # here cls is class argument that we are passing and string is second argument
        import re
        item = re.findall('is \w*', string)
        name = item[0][3:]
        price = item[1][3:]
        return clr(name,int(price))
    
    @staticmethod
    def printstatement(): 
    # code will run even if we dont pass any parameters to static method i.e by default it doesnt require any argument
        print("This is static method")
        
        
        
    def discountedPrice(self):
        # disc_amt = (self.discount/100) * self.price <--- if we use this only class variable 10% will be used
        disc_amt = (self.discount/100) * self.price
        finalAmt = self.price - disc_amt
        return round(finalAmt,3)
    

l1 = Laptop.from_string("Laptop name is MacbookPro and price is 200000")
print(l1.__dict__)

l2 = Laptop("HP", 70000)
print(l2.__dict__)

l2.discount =5
print(l2.__dict__)
print(l2.discountedPrice())

print(l2.printstatement())