# functions go here

# makes it that fields cannot be empty, or filled with spaces
def not_blank(question, error_msg):
    valid = False

    while not valid:
        response = input(question)

        if response == "":
            print(error_msg)
        
        # credit: Ryan Ogilvy; for the whitespace checker
        elif str.isspace(response):
            print(error_msg)
        else:
            return response
  


# start of loop

# initialise loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count <= MAX_TICKETS - 1:

    # get details
    name = not_blank("What is your name? ", "Your name cannot be blank, please enter a new name.")
    count += 1
