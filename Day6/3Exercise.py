class students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def result(self):
        if self.marks < 500:
            return "Fail"
        else:
            return "Pass"
        
s1 = students("Shubham", 500)
s2 = students("Pavani", 510)
s3 = students("bawankule", 400)
s4 = students("karthika", 550)
s5 = students("divya", 300)
s6 = students("rajat", 700)
s7 = students("pallavi", 499)
s8 = students("keshav", 501)

student_object = [s1, s2, s3, s4, s5, s6 ,s7, s8]

passStudents= []
failStudents= []
students_results= {}

for x in student_object:
    if x.result() == "Pass":
        passStudents.append(x.name)
        students_results['Pass Students']= passStudents
    else:
        failStudents.append(x.name)
        students_results['Failed Students']= failStudents
        
print(students_results)
        
        