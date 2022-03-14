"""
string_eksempel = "eksempel"
print(string_eksempel.capitalize())
print(string_eksempel.isupper())

names = ["nicklas", "benjamin", "Micael", "claus"]
for name in names:
    if name[0].isupper():
        continue
    else:
        print(name.capitalize())

#Nested if -> and
user_age = int(input("How old are you?"))
residence_permit = input("Do you have a residence permit")

if user_age >= 17 and residence_permit == "yes":
        print("Inside here - you can apply")
"""

#Not operator
#user_input = input("What is your age?") #is input numeric?
user_input = input("Age?")

if user_input.isnumeric():
    print("User input is numeric")
else:
    print("Wrong input format")

#While input is not

#in list, not in list