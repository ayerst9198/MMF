import re


# functions go here
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


# Valid options for yes / no questions
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# initialise variables
snack_ok = ""
snack = ""


# ask user if they want snacks
check_snack = "invalid choice"
while check_snack == "invalid choice":
    want_snack = input("Do you want snacks? ").lower()
    check_snack = string_checker(want_snack, yes_no)
    if check_snack == "invalid choice":
        print("Please enter yes or no")

# if they say yes ask what snacks they want
if check_snack == "Yes":
    get_order = get_snack()

else:
    get_order = []

# show snack orders
print()
if len(get_order) == 0:
    print("Snacks Ordered: None")

else:
    print("Snacks Ordered:")
    print(get_order)
