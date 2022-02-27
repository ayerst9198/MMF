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

# Main Routine 

# regular expressoin to find if item starts with a number
number_regex = "^[1-9]"

# valid snacks holds list of all snacks
# Each item in valid snacks is a list whith
# valid options for each snack <full name, letter  code (a - e)
# , and possible abbreviatio
valid_snacks = [
    ["popcorn", "p", "corn", "a"], 
    ["M&M's", "m&m's", "mms", "m", "b"], 
    ["pita chips", "chips", "pc", "pita", "c"], 
    ["water", "w", "d"],
    ["orange juice", "oj", "o", "juice", "e"]
]

# Valid options for yes / no questions
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]


# initialise variables
snack_ok = ""
snack = ""
snack_list = []

# ask user if they want snacks
check_snack = "invalid choice"
while check_snack == "invalid choice":
    want_snack = input("Do you want snacks? ").lower()
    check_snack = string_checker(want_snack, yes_no)
    if check_snack == "invalid choice":
        print("Please enter yes or no")




# loop 3 times to make testing quicker
if check_snack == "Yes":
    # ask user for a desired snacks and put in lowercase
    snack_ok = "no"

    desired_snack = ""
    while desired_snack != "xxx":

        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            break
        
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
        amount_snack = "{} {}".format(amount, snack_choice)

        # check snack is not exit code before adding
        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_list.append(amount_snack)

# show snack orders
print()
if len(snack_list) == 0:
    print("Snacks Ordered: None")

else:
    print("Snacks Ordered:")

    for item in snack_list:
        print(item)

