# import pprint
import requests
import json
import html
import random

# api
url = "https://opentdb.com/api.php?amount=1"
# to stop execution/ exit loop
endgame = ""
score_correct = 0
score_incorrect = 0

print("This program gives you a trivia")
input("press any key if you are ready to play...." + "\n")

while endgame != "quit":
    opt = 1
    r = requests.get(url)
    if r.status_code != 200:
        endgame = input("Sorry something went wrong, press enter to try again, or type quit to end. ").lower()
    else:
        quiz_data = json.loads(r.text)
        # pprint.pprint(quiz_data)
        # input("Press enter to get a new question")
    data_val = False
    question = quiz_data['results'][0]['question']
    answers = quiz_data['results'][0]['incorrect_answers']
    correct_ans = quiz_data['results'][0]['correct_answer']
    answers.append(correct_ans)
    random.shuffle(answers)

    print(html.unescape(question) + "\n")
    print("Options :")
    for answer in answers:
        print(str(opt) + "-", html.unescape(answer))
        opt += 1

    # answer = correct_ans
    while data_val == False:
        guess = input("\nEnter your answer number: ")
        try:
            guess = int(guess)
            if guess > len(answers) or guess <= 0:
                print("invalid answer, input must be integer between options 1-4")
            else:
                data_val = True
        except:
            print("input must be integer between options 1-4")
            continue
    guess = answers[int(guess)-1]

    if guess == correct_ans:
        print("Correct, the right answer is " + correct_ans)
        score_correct += 1
    else:
        print("Wrong, the correct answer is " + (quiz_data['results'][0]['correct_answer']))
        score_incorrect += 1

    print("\n######################################")
    print("Your Score is :")
    print("correct answers: " + str(score_correct), "\nincorrect answers: " + str(score_incorrect))
    print("######################################\n")

    endgame = input("Press enter if you want to try another question or  type quit to exit.").lower()

print("\n Thanks for playing.")
