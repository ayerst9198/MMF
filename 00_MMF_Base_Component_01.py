# import statements


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


# *********** Main Routine ***********

# Set up Dictionaries / lists needed to hold data

# Ask user if they have used the program before & show instructions if they haven't

# Loop to get ticket details

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

    # Get name (can't be blank)
    name = not_blank("What is your name? ", "Your name cannot be blank, please enter a new name.")

    # implements exit code
    if name == "xxx":
        break
    
    # increases the number of seats purchased by 1
    count += 1
    print()

# checks if seats left = 1, if so prints a special message
if count == MAX_TICKETS:
    print("You have sold all available tickets!")
else:
    print("You have sold {} tickets. There are still {} tickets available".format(count, MAX_TICKETS - count))


    # Get age (between 12 and 130)

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method

    # Calculate total sales and profit

# Outpuyt data to text file