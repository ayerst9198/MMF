import random
import time
responses = ["Not so sure", "42", "Most likely", "Absolutely not", "Outlook is good", "I see good things happening", "Never",
"Negative", "Could be", "Unclear, ask again", "Yes", "No", "Possible, but not probable"]

## Following function asks user question, then returns random results from responses
def answerQuery():
    question = input("Ask and you shall receive: ")
    print()
    print(random.choice(responses))
    print("\n")
answerQuery()

## Following asks user if they would like to play again, and loops until user is finished
secondQuestion = str("Y")
while secondQuestion == str("Y"):
    answerQuery()
