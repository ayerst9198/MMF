# functions go here

# taken from RPS
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please input yes / no")

# Main Routine Goes Here

for item in range (0, 6):
    want_snacks = yes_no("Do you want snacks? ")
    print("Answer OK, you said:", want_snacks)
    print()