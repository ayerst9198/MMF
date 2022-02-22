# functions go here
def string_checker(question, to_check):
    valid = False
    while not valid:
        response = input(question).lower()

        if response in to_check:
            print("checked", response)
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
    print("check snack", check_snack)


# loop 3 times to make testing quicker
if check_snack == "Yes":
    # ask user for a desired snacks and put in lowercase
    snack_ok = "no"

    desired_snack = ""
    while desired_snack != "xxx":

        desired_snack = input("Snack: ").lower()

        # if snack is in one of the lists, return full snack
        for var_list in valid_snacks:
            if desired_snack in var_list:

                # Get full name of snack and put it in title
                snack = var_list[0].title()
                snack_list.append(var_list[0].title())
                snack_ok = "yes"
            #     break

        # # if the chosen snackis not valid, set snack_ok to "no"
        # else:
        #     snack_ok = "no"
        #     break
    
    # if the snakc != ok - ask again
    if snack_ok == "yes":
        print("Snack Choice: ", snack)
    else:
        print("invalid_choice")
print("Sold snacks: {}".format(snack_list))
