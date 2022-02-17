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
count = 0
while 1 == 1:
    want_snacks = yes_no("Do you want snacks? ")
    print("Answer OK, you said:", want_snacks)
    print()
    if want_snacks == "yes":
        count += 1
    if count == 6:
        print("You a greedy lil mf aren't ya")
        break