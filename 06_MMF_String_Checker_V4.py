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
    else: return "invalid choice"

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

# holds snack order for a single user
snack_order = []

# ask user if they want a snack
check_snack = "invalid choice"
while check_snack == "invalid choice":
    want_snack = input("Do you want snacks? ").lower()
    check_snack = string_checker(want_snack, yes_no)


# if they say yes, ask what snack they want
if check_snack == "Yes":

    desired_snack = ""
    while desired_snack != "xxx":

        # ask user for desired snack and put it in lowercase
        desired_snack = input("Snack: ").lower

        if desired_snack == "xxx":
            break
        
        # check snack choice isvalid
        snack_choice = string_checker(desired_snack, valid_snacks)
        print("Snack Choice: ", snack_choice)
    
    # add snack to list

    # check that snack is not exit code before adding
    if snack_choice != "xxx" and snack_choice != "invalid choice":
        snack_order.append(snack_choice)
# initialise variables
snack_ok = ""
snack = ""
snack_list = []

#show snakck orders
print()
if len(snack_order) == 0:
    print("Snacks Ordered: None")
else:
    print("Snacks Ordered:")

    for item in snack_order:
        print(item)