class phone:
    def __init__(self,brand, modelname, price):
        self.brand = brand
        self.modelname = modelname
        self.price = max(price,0)
    @staticmethod   
    def makecall(phonenum):
        print(f'calling number {phonenum}...')
        
    def fullname(self):
        return f"{self.brand} {self.modelname}"
    
    
class smartphone(phone):
    def __init__(self,brand, modelname, price, ram ,internal_memory, rear_camera):
        phone.__init__(self,brand,modelname,price)
        # or super.__init(self,brand,modelname,price)
        # self.brand = brand
        # self.modelname = modelname
        # self.price = max(price,0)
        
        # above 3 lines are reduntant in both classes
        self.ram = ram
        self.inetrnal_memory = internal_memory
        self.rear_camera = rear_camera
        
    @staticmethod   
    def makecall(phonenum):
        print(f'calling number {phonenum}...')
        
    def fullname(self):
        return f"{self.brand} {self.modelname}"
    
smartphone1= smartphone('samsung','A5',55000,'12GB','256GB','50MP')

print(smartphone1.__dict__)