# Helps reduce redundancy of code

class student:
    totalMarks = 1000   #<---- class variable
    # def __init__(self, name, age, marks, totalMarks):
    def __init__(self, name, age, marks): #<--- instead of giving parameter here- we give a class variable 
        self.name = name
        self.age = age
        self.marks = marks
        # self.totalMarks = totalMarks       # <---- we can use it like this but have to define it for everu object created
        self.totalMarks = student.totalMarks

# s1= student("Shubham", "25", 700, 1000) #<-- we would have given total marks in each object
s2= student("bawankule", "26", 750)

print(s2.totalMarks)