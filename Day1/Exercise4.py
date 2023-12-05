# Lists and Tuples
# Program to print Birth-month from tuple

months = ("january", "february", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December")

birthDate = input("Enter your Birth Date DD-MM-YYYY: ")

index = int(birthDate[3:5])-1

bd_month = months[index]

print(bd_month)

# People = ["shubham", "SHubham", "SHUbham"]
# new = input("Enter Your Name: ")
# People.append(new)
# print(People)
