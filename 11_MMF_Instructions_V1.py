
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


def instructions(options):
    show_help = "invalid choice"

    while show_help == "invalid choice":
        show_help = input("Would you like to read the instructions? ")
        show_help = string_checker(show_help, options)

        if show_help == "Yes":
            print()
            print("***INSTRUCTIONS GO HERE***")
            print()
            return ""
        
        elif show_help == "No":
            return ""

        elif show_help == "invalid choice":
            print("Please enter y/n")
            continue
        
        return ""



# ******** MAIN ROUTINE *********

yes_no = [
    ["yes", "y"],
    ["no", "n"]
]


while 1 == 1:
    
    instructions(yes_no)
    print("program continues")