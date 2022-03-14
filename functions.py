#Takes two names, returns full name capitalized
def capitalize_full_name(first_name, last_name):
    return str(first_name).capitalize() + " " + str(last_name).capitalize()

print(capitalize_full_name("nicklas","frederiksen"))

#nem-id validation
def validate_nem_id(user_input):
    # length is correct & is numeric
    if len(str(user_input)) == 10 and str(user_input).isnumeric():
        return True
    else:
        return False

user_input = input("What is your nem-id?")
if validate_nem_id(user_input):
    print("You are now logged in")
else:
    print("Wrong input")