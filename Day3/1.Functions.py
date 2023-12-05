# for adding functions which we can use multiple times in python "def" is used

# /creating function without parameter
def say_hello():
    print("Hello World")


# /utilising function
say_hello()


# /creating function with parameter

def hello(person1, person2):
    print("Hello", person1, ",", person2, "is waiting for you")


hello("steve", "robin")


def hello1(person1, person2="Steve"):
    print("Hello", person1, ",", person2, "is waiting for you")


hello1("Momo")


def fahrtocelsius(fahr):
    celsius = (5 * (fahr - 32)) / 9
    return celsius


print(fahrtocelsius(80))
print("Celsius", round(fahrtocelsius(100), 2))
print("Kelvin", round(fahrtocelsius(100) + 273.5, 2))

