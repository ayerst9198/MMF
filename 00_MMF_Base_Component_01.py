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

    # Get name (can't be blank)
    name = not_blank("name: ", "no blanks, sorry")

    # Get age (between 12 and 130)

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method

    # Calculate total sales and profit

# Outpuyt data to text file