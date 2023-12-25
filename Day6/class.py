
# defining a class in python

class student:
    def __init__(self, name, rollNum, marks): # <--- constructor in python having different attributes
        self.name = name
        self.rollNum = rollNum
        self.marks = marks
        
student1 = student("Shubham", 25, 500)  # we ncan make n number of objects using this constructor 
student2 = student("Bawankule", 26, 600)

print(student1.name)
print(student2.name)

# Example

class product:
    def __init__(self, productName, brandName, modelName, price): #defined attributes are 4 actual attributes 5 in thi example
        self.productName = productName
        self.brandName = brandName
        self.modelName = modelName
        self.price = price
        self.productNamewithPrice = productName +" " + str(price) # we can concatenate attributes

product1 = product("Iphone", "Apple", "15pro", 150000)
product2 = product("Pixel", "Google", "8pro", 100000)

print(product1.productName)
print(product2.price)
print(product1.productNamewithPrice)


