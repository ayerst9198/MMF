



# Function goes here
#WARNING: The response is returned in title case
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

pay_method = [
    ["cash", "ca"],
    ["credit", "cr"]
]

# Loop until exit code...
name = ""
while name != "xxx":
    name = input("Name: ")
    print()
    if name == "xxx":
        break

    # ask for payment method
    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method (cash or credit): ")
        print()
        how_pay = string_checker(how_pay, pay_method)
    
    # Ask for subtotal (for testing purposes)
    subtotal = float(input('Sub total? $'))
    print()

    if how_pay == "Credit":
        surcharge = 0.05 * subtotal
    else:
        surcharge = 0
    
    total = subtotal + surcharge
    print("Name: {} | Subtotal: ${:.2f} | Surcharge ${:.2f} | Total Payable: ${:.2f}".format(name, subtotal, surcharge, total))
    print()
    print()