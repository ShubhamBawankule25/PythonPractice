class student:
    def __init__(self, name, rollNum, marks): # <--- constructor in python having different attributes/parameter
        self.name = name
        self.rollNum = rollNum
        self.marks = marks

    def result(self):                #<------ method for this calss showing passing criteria
        if self.marks < 500:
            return "Fail"
        else:
            return "Pass"
        
s1 = student("shubham", 25, 500)
s2 = student("bawankule", 26, 499)

print(s1.result())

print(s2.result())
