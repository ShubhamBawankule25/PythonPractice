# Dictionary

person = {"firstName": "John", "lastName": "Legend", "birthYear": 1980}
print(person)

person["birthYear"] = 1979
print(person)

person["maritalStatus"] = "Married"
print(person)

person["children"] = ["ana", "tina"]
print(person)

person["children"].append("ana")
print(person)

# person["age"] running this will give error in program so alternative way to get is
print(person.get("age", "Invalid value"))

key = "firstName"
print(person[key])

# to clear a dictionary
# person.clear()
