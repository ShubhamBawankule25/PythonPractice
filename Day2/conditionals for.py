blog_Posts = ["sentence 1", "Sentence 2", "Sentence 3", "", "Sentence 4"]
for post in blog_Posts:
    if post == "":
        continue
    else:
        print(post)

print('__________________________________________')

myString = "This is a string"

for char in myString:
    # if char == " ":
    #     continue
    # else:
        print(char)

print('__________________________________________')

for x in range(0,10):
    print(x)

print('__________________________________________')

person = {"Name": "ABC", "Age": 25, "Gender": "Male"}

for key in person:
    print(key, ":", person[key])

print('__________________________________________')

blog_Posts = {"Python":["sentence 1", "Sentence 2", "Sentence 3", "", "Sentence 4"],
              "Javascript":["sentence 1", "Sentence 2", "Sentence 3", "", "Sentence 4"]}

for category in blog_Posts:
    print("Post about,", category)
    for post in blog_Posts[category]:
        if post == "":
            continue
        else:
            print(post)

