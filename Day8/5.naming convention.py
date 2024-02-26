# In pythonn every variable is public
# so to generally use/show an variable as private we use _var name ,
# it doesnt change type from public to private, just a best bractice.

class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
        self._discount = 5
        
    def applyDisc(self):
        return self.price - (self.price * (self._discount /100))
        
Phone1= Phone('samsung', 'a5', 50000)

print(Phone1.__dict__)

print(Phone1.applyDisc())

Phone1._discount = 10

print(Phone1.applyDisc())
