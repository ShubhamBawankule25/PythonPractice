class product:
    def __init__(self, productName, price):
        self.productName = productName
        self.price = price
        self.productnamewithprice = productName + str(price)
        
        
    def discount(self, discountvalue):
        discountAmt = (self.price/100)*discountvalue
        final_price = self.price - discountAmt
        return int(final_price)
    
mobile = product("Iphone15", 150000)

laptop = product("Acer Nitro 5", 70000)

print(laptop.discount(20))

print(mobile.discount(10))
