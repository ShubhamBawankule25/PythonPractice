class Date:         # constructor / init method
    def __init__(self,year, month, day):
        self.year = year
        self.month = month
        self.day = day
        
    
    def arrangeIntoDatePattern(self):   # instance method as it contains self as constraint
        date = f"{self.day}-{self.month}-{self.year}"
        return date
        
date1 = Date(2024, 0o1, 0o4)

print(date1.__dict__)

print(date1.arrangeIntoDatePattern())