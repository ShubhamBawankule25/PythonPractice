import requests
import json
import pprint

# getting api request pulled for trivia app
r = requests.get("https://opentdb.com/api.php?amount=1&category=27&difficulty=easy&type=multiple")

# api response code 
print(r.status_code)

# what api returns
print(r.text)

# checking type of what api returned 
print(type(r.text))

# importing returned json as dictionary
question = json.loads(r.text)

print(question)

# formatting data to make it easier to understand
pprint.pprint(question)

# from the data which is dictionary returning required info
# question = dictionary, [results] = key (of type list of dictionary), [0] = index of first element in results, [] = key 
print(question['results'][0]['incorrect_answers'])


