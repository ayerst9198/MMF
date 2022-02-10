# functions go here

def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response == "":
            print("No blanks, sorry")            
        else:
            return response
            

# Main routine goes here
name = not_blank("name: ")
print()
print("Your name is:",name)