# functions go here
def string_checker(question, to_check):
    valid = False
    while not valid:
        response = input(question).lower()

        if response in to_check:
            return response
        
        else:
            for item in to_check:
                #checks if response is first letter in item in valid response list
                if response == item[0]:
                    #note returns entire response
                    return item

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

# initialise variables
snack_ok = ""
snack = ""

# loop 3 times to make testing quicker
for item in range(0, 3):
    # ask user for a desired snacks and put in lowercase
    desired_snack = input("Snack: ").lower()

    for var_list in valid_snacks:

        # if snack is in one of the lists, return full snack
        if desired_snack in var_list:

            # Get full name of snack and put it in title
            snack = var_list[0].title()
            snack_ok = "yes"
            break

        # if the chosen snackis not valid, set snack_ok to "no"
        else:
            snack_ok = "no"
            break
    
    # if the snakc != ok - ask again
    if snack_ok == "yes":
        print("Snack Choice: ", snack)
    else:
        print("invalid_choice")
