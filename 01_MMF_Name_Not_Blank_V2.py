# functions go here

def not_blank(question, error_msg):
    valid = False

    while not valid:
        response = input(question)

        if response == "":
            print(error_msg)            
        else:
            return response
            

# Main routine goes here

while 1 == 1:
    name = not_blank("name: ", "no blanks, sorry")
    print()
    print("Your name is:",name)
    print()
    print()