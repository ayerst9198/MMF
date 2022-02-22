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

# valid snacks holds list of all snacks
# Each item in valid snacks is a list whith
# valid options for each snack <full name, letter  code (a - e)
# , and possible abbreviatio
valid_snacks = [
    ["popcorn", "p", "corn", "a"], 
    ["M&M's", "m&m's", "mms", "m", "b"], 
    ["pita chips", "chips", "pc", "pita", "c"], 
    ["water", "w", "d"]
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


# loop 3 times to make testing quicker
if check_snack == "Yes":
    # ask user for a desired snacks and put in lowercase
    snack_ok = "no"

    desired_snack = ""
    while desired_snack != "xxx":

        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            break

        snack_choice = string_checker(desired_snack, valid_snacks)
        print("snack choice: ", snack_choice)
        snack_list.append(snack_choice)

print("Sold snacks: {}".format(snack_list))

