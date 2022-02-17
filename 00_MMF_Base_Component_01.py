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

# makes sure that the number entered is between the highest number alloiwed and the lowestnumber allowed, with an exit code
# taken from year 10 programming assessment
def num_check(question, num_type, error, low=None, high=None, exit_code=None):

    valid = False
    while not valid:
        try:
            response = input(question).lower()


            if response == exit_code:
                return response

            else:
                response = num_type(response)
 
            if low is not None and high is not None:
                if low <= response <= high:
                    return response
                else:
                    print(error)
                    print()
                    continue

            elif low is not None:
                if response >= low:
                    return response
                else:
                    print(error)
                    print()
                    continue

            elif high is not None:
                if response <= high:
                    return response
                else:
                    print(error)
                    print()
                    continue

            else:
                return response

        except ValueError:
            print(error)
            print()


# *********** Main Routine ***********

# Set up Dictionaries / lists needed to hold data

# Ask user if they have used the program before & show instructions if they haven't

# Loop to get ticket details

# initialise loop so that it runs at least once
name = ""
ticket_count = 0
profit = 0
MAX_TICKETS = 5

while name != "xxx" and ticket_count <= MAX_TICKETS - 1:

    

    if MAX_TICKETS - ticket_count == 1:
        print ("ONLY 1 TICKET LEFT")
    else:
        print("You have {} seats left".format(MAX_TICKETS - ticket_count))

    # get details

    # Get name (can't be blank)
    name = not_blank("What is your name? ", "Your name cannot be blank, please enter a new name.")

    print()

    # implements exit code
    if name == "xxx":
        break
    

    # checks the users age to make sure that they are between the ages of 12 and 130
    age = num_check("What is your age? ", int, "Only those between ages 12 and 130 are permitted to purchase seats. Please enter an integer between 12 and 130.")

    print()

    # if the age given is below 12 or above 130, an error is printed which sends the user back to the input name.
    if age < 12 or age > 130:
        print("Only those between ages 12 and 130 are permitted to purchase seats.")
        print()
        continue

    # cost depending on age
    elif age < 16:
        ticket_price = 7.50
    elif age > 64:
        ticket_price = 6.50
    else:
        ticket_price = 10.50

    # calculates the profit made from the tickets sold
    profit_made = ticket_price - 5
    profit += profit_made

    # increases the number of seats purchased by 1
    ticket_count += 1
    print()


        

# checks if seats left = 1, if so prints a special message
if ticket_count == MAX_TICKETS:
    print("You have sold all available tickets!")
else:
    print("You have sold {} tickets. There are still {} tickets available".format(ticket_count, MAX_TICKETS - ticket_count))

# says how much profit has been made
print()
print("$$$$$ You have made ${:.2f} profit $$$$$".format(profit))
print()