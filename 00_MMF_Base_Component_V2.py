# import statements
import re
import pandas

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

# checks number of tickets left, and warns user
def check_tickets(tickets_sold, ticket_limit):
    # tells user how many seats are left
    if ticket_limit - tickets_sold == 1:
        print ("ONLY 1 TICKET LEFT")
    else:
        print("You have {} seats left".format(ticket_limit - tickets_sold))


# Gets ticket price based on age
def get_ticket_price():

    # get age (between 12 and 130)
    age = num_check("Age: ", int, "Please enter an integer")

    # if the age given is below 12 or above 130, an error is printed which sends the user back to the input name.
    if age < 12 or age > 130:
        print("Only those between ages 12 and 130 are permitted to purchase seats.")
        print()
        return "invalid ticket price"

    # cost depending on age
    elif age < 16:
        ticket_price = 7.50
    elif age > 64:
        ticket_price = 6.50
    else:
        ticket_price = 10.50
    
    return ticket_price
    

# *********** Main Routine ***********

# Set up Dictionaries / lists needed to hold data
name = ""
ticket_count = 0
ticket_sales = 0
MAX_TICKETS = 5

# initialise lists
all_names = []
all_tickets = []

# data frame dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets
}

# Ask user if they have used the program before & show instructions if they haven't


# initialise loop so that it runs at least once
while name != "xxx" and ticket_count <= MAX_TICKETS - 1:

    
    # tells user how many seats are left
    check_tickets(ticket_count, MAX_TICKETS)
    
    # get details

    # Get name (can't be blank)
    name = not_blank("What is your name? ", "Your name cannot be blank, please enter a new name.")

    print()

    # implements exit code
    if name == "xxx":
        break
    

    # gets ticekt price based on age
    ticket_price = get_ticket_price()

    # if age is invalid, restart loop
    if ticket_price == "invalid ticket price":
        continue

    # increases the number of seats purchased by 1
    ticket_count += 1
    ticket_sales += ticket_price

    # adds names and ticket prices to lists
    all_names.append(name)
    all_tickets.append(ticket_price)

    # get snacks

    # Get payment method (ie: work out if surcharge is needed)\

# end of tickets/snacks/payment loop

# print details
movie_frame = pandas.DataFrame(movie_data_dict)
print(movie_frame)

# Calculate ticket profit...
ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))

# Tell user if they have unsold tickets
if ticket_count == MAX_TICKETS:
    print("You have sold all available tickets!")
else:
    print("You have sold {} tickets. There are still {} tickets available".format(ticket_count, MAX_TICKETS - ticket_count))
