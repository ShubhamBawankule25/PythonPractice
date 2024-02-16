# Encapsulation = keping all attributes in same class(in laymans terms)
#Abstrraction = giving access to only required methods or functions

class phone:
    def __init__(self,brand, modelname,price):
        self.brand = brand
        self.modelname = modelname
        self.price = price
    @staticmethod   
    def makecall(phonenum):
        print(f'calling number {phonenum}...')
        
    def fullname(self):
        return f"{self.brand} {self.modelname}"
    
phone1 = phone('Nokia', 1100, 44000)

phone1.makecall('8806853439')

print(phone1.fullname())
