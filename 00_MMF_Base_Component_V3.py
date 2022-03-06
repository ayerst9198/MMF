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

def string_checker(choice, options):
    for var_list in options:

        # if snack is in list return full snack name
        if choice in var_list:

            # get full name of snack and put it 
            # in title case so it looks noice
            chosen = var_list[0].title()
            is_valid = "yes"
            break
        # if choe option is not valid, set is_valid to no
        else:
            is_valid = "no"
    
    # if snack is not ok - ask again
    if is_valid == "yes":
        return chosen
    else: 
        return "invalid choice"

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
    
# Gets list of snacks
def get_snack():
        
    # Main Routine 

    # regular expressoin to find if item starts with a number
    number_regex = "^[1-9]"

    # valid snacks holds list of all snacks
    # Each item in valid snacks is a list whith
    # valid options for each snack <full name, letter  code (a - e)
    # , and possible abbreviation

    valid_snacks = [
        ["popcorn", "p", "corn", "a"], 
        ["M&M's", "m&m's", "mms", "m", "b"], 
        ["pita chips", "chips", "pc", "pita", "c"], 
        ["water", "w", "d"],
        ["orange juice", "oj", "o", "juice", "e"]
    ]



    snack_list = []

    desired_snack = ""
    while desired_snack != "xxx":

        snack_row = []

        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            return snack_list
        
        # if item has a number, seperate it into two (number/snack)
        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]
        else:
            amount = 1
            desired_snack = desired_snack
        
        # remove white space around snack
        desired_snack = desired_snack.strip()

        # check snack is valid
        snack_choice = string_checker(desired_snack, valid_snacks)

        if snack_choice == "invalid choice":
            print("Please enter a valid snack")
        
        # check amount is valid (less than 5)
        if amount >= 5:
            print("Sorry - we have a 4 snack maximum")
            snack_choice = "invalid choice"
        
        # add snack and amount to list...
        snack_row.append(amount)
        snack_row.append(snack_choice)

        # check snack is not exit code before adding
        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_list.append(snack_row)

# *********** Main Routine ***********

# Set up Dictionaries / lists needed to hold data
name = ""
ticket_count = 0
ticket_sales = 0
MAX_TICKETS = 5

# initialise lists
pay_method = [
    ["cash", "ca"],
    ["credit", "cr"]
]
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]
all_names = []
all_tickets = []
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []


snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

# data frame dictionary
movie_data_dict = {
    "Name": all_names,
    "Ticket": all_tickets,
    "Popcorn": popcorn,
    "Water": water,
    "Pita Chips": pita_chips,
    "M&M's": mms,
    "Orange Juice": orange_juice
}

# price dictionary
price_dict = {
    "Popcorn": 2.5,
    "Water": 2,
    "Pita Chips": 4.5,
    "M&M's": 3,
    "Orange Juice": 3.25
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
    # ask user if they want a snack
    check_snack = "invalid choice"
    while check_snack == "invalid choice":
        want_snack = input("Do you want to order snacks? ")
        check_snack = string_checker(want_snack, yes_no)
    
    # If they say yes, ask what snacks they want
    if check_snack == "Yes":
        snack_order = get_snack()
    else:
        snack_order = []

    # assume no snacks have been bought
    for item in snack_lists:
        item.append(0)

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount

    # Get payment method (ie: work out if surcharge is needed)
        # ask for payment method
    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method (cash or credit): ").lower()
        print()
        how_pay = string_checker(how_pay, pay_method)
    
    if how_pay == "Credit":
        surcharge_multiplier = 0.05
    else:
        surcharge = 0

# end of tickets/snacks/payment loop

# print details
# create a dataframe and set the index to name column
movie_frame = pandas.DataFrame(movie_data_dict, columns=['Name', "Ticket", 'Popcorn', 'Water', "Pita Chips", "M&M's", "Orange Juice"])
movie_frame = movie_frame.set_index("Name")

# create a column called "subtotal"
# fill with price for snacks and ticket

movie_frame["Subtotal"] = \
    movie_frame["Ticket"] + \
    movie_frame["Popcorn"]*price_dict["Popcorn"] + \
    movie_frame["Water"]*price_dict["Water"] + \
    movie_frame["Pita Chips"]*price_dict["Pita Chips"] + \
    movie_frame["M&M's"]*price_dict["M&M's"] + \
    movie_frame["Orange Juice"]*price_dict["Orange Juice"]


# shorten column names
movie_frame = movie_frame.rename(columns={"Orange Juice": "OJ", "Pita Chips": "Chips"})

print(movie_frame)

# Calculate ticket profit...
ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))

# Tell user if they have unsold tickets
if ticket_count == MAX_TICKETS:
    print("You have sold all available tickets!")
else:
    print("You have sold {} tickets. There are still {} tickets available".format(ticket_count, MAX_TICKETS - ticket_count))
