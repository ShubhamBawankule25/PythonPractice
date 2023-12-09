person = {"name": "John", "gender": "Male", "age": 25, "address": "116,sankalp nagar", "phone": "8806853439"}
# print(person)

# Stupid way

# name = "Name"
# Gender = "gender"
# Age = "age"
# Address = "address"
# Phone = "phone"
#
# prompt = input("What you want to know: ")
# print("Your requested information: ", person[prompt])

key = input("Your requested information: ").lower()

result = person.get(key, "Invalid")
print(result)
