#functions go here

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

# main routine goes here

for item in range (0, 6):
    want_snacks = string_checker("Do you want snacks? ", ["yes", "no"])

    print()
    print("Answer OK, you said:", want_snacks)
    print()