class Date:         # constructor / init method
    def __init__(self,year, month, day):
        self.year = year
        self.month = month
        self.day = day
        
    
    def arrangeIntoDatePattern(self):   # instance method as it contains self as constraint
        date = f"{self.day}-{self.month}-{self.year}"
        return date
    
    @classmethod
    def getDataFromString(cls, string):
        import re
        date = re.findall('\d{2}-\d{2}-\d{4} | \d{2}/\d{2}/\d{4}')[0]
        listDate = date.replace('/', '-').split('-')
        date = listDate[0]
        month = listDate[1]
        year = listDate[2]
        return cls(date, month, year)
        
        
date1 = Date(2024, 0o1, 0o4)

print(date1.__dict__)

print(date1.arrangeIntoDatePattern())