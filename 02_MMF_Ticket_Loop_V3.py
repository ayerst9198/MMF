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

    

    if MAX_TICKETS - count == 1:
        print ("ONLY 1 TICKET LEFT")
    else:
        print("You have {} seats left".format(MAX_TICKETS - count))

    # get details
    name = not_blank("What is your name? ", "Your name cannot be blank, please enter a new name.")
    # implements exit code
    if name == "xxx":
        break
    count += 1
    print()

if count == MAX_TICKETS:
    print("You have sold all available tickets!")
else:
    print("You have sold {} tickets. There are still {} tickets available".format(count, MAX_TICKETS - count))
