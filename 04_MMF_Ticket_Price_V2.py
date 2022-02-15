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


# Main Routine

test = True

# loops for testing
while test == True:
    profit = 0
    
    print()

    # asks user for their name, with no blanks
    name = not_blank("name: ", "no blanks, sorry")

    if name == "xxx":
        break

    print()

    age = num_check("How old are you? ", int, "Please enter an integer between 12 and 130", 12, 130, "xxx")
    print()

    # if the age given is below 12 or above 130, an error is printed which sends the user back to input name.
    if age < 12 or age > 130:
        print("Only those between ages 12 and 130 are permitted to purchase seats.")
        print()
        continue
    elif age < 16:
        ticket_price = 7.50
    elif age > 64:
        ticket_price = 6.50
    else:
        ticket_price = 10.50
    
    profit_made = ticket_price - 5
    profit += profit_made

    # prints the cost, displayed as a price
    print("***** {} has purchased a ticket. The cost is: ${:.2f}".format(name, ticket_price) + " *****")
    print()
    print("You have made ${:.2f} profit".format(profit))