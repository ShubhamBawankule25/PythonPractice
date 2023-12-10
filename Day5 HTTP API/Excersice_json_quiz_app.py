import requests
import json
import random
# import pprint

url = "https://opentdb.com/api.php?amount=1&category=27&difficulty=easy&type=multiple"

endgame = ""



print("This program gives you a trivia to play.")
input("press any key if you are ready to play....")


while endgame!= "quit":
    
    r = requests.get(url)
    if r.status_code != 200:
        endgame = input("Sorry something went wrong, press enter to try again, or type quit to end. ")
    else:
        quiz_data = json.loads(r.text)

    print(quiz_data['results'][0]['question'], ":")
    print("Options :")
    
    options = (quiz_data['results'][0]['incorrect_answers'][0], 
          (quiz_data['results'][0]['correct_answer']) , ":")
    
    answer = (quiz_data['results'][0]['correct_answer'])
    guess = input("Enter your answer: ")
    if guess == answer:
        print("Correct, thats the right answer")
        break
    else:
        print("Wrong, the correct answer is" + (quiz_data['results'][0]['correct_answer']))
        
    

