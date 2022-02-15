# functions go here

# makes sure that the number entered is between the highest number alloiwed and the lowestnumber allowed, with an exit code
# taken from year 10 programming assessment
def num_check(question, num_type, error, low=None, high=None, exit_code=None):

    valid = False
    while not valid:
        try:
            response = input(question).lower()


            if response == exit_code:
                return response

            else:
                response = num_type(response)
 
            if low is not None and high is not None:
                if low <= response <= high:
                    return response
                else:
                    print(error)
                    print()
                    continue

            elif low is not None:
                if response >= low:
                    return response
                else:
                    print(error)
                    print()
                    continue

            elif high is not None:
                if response <= high:
                    return response
                else:
                    print(error)
                    print()
                    continue

            else:
                return response

        except ValueError:
            print(error)
            print()

age = "yes"

# loops for testing
while age != int:
    age = num_check("How old are you? ", int, "Please enter an integer between 12 and 130", 12, 130, "xxx")
    if age == "xxx":
        break
    print()
    print("***** You are {} years old *****".format(age))
    print()