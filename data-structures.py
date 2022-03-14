#Slicing and index

participants_list = ["Nicklas", "Jarl", "Benjamin", "Claus"]
participants_tupple = ("Nicklas", "Jarl", "Benjamin", "Claus")

"""
first_participant = participants_list[0]
first_two_participants = participants_list[0:2]
print(first_two_participants)


#Append - add an element
late_registered_participant = "Francis"
participants_list.append(late_registered_participant)

#Pop - remove an element
participants_list.pop(-2)
print(participants_list)

#Extend
participants_2 = ["Lorena", "Marianne", "Dicte"]
participants_list.extend(participants_2)
print(participants_list)


#Split string
tool_order = "keyboard, keyboard, keyboard, mouse, mouse, screen, trackpad"
order_list = tool_order.split(",")
print(order_list)
"""

#Sort
# price_list = [50, 12, 42, 15, 633, 421, 55, 35, 321]
# price_list.sort(reverse=True)
# print(price_list)

#List inside list
# car_1 = ["Hyundai i10", 9248]
# car_2 = ["Citroen c1", 5311]
# car_3 = ["Volkswagen UP", 0]

#A dictionary
my_dict = {
    "chili": "En rød pebberfrugt, der er stærkere end normale pepperfrugter",
    "bord": "En flade på fire ben, der løfter indhold",
    "pære": "En elektrisk glødetråd med omkransende glassfære omkring"
}

# print(my_dict.get("chili"))

#Postnummer
postnumre = {
    2830: "Virum",
    2660: "Brøndby Strand",
    2200: "København N",
    1218: "København K",
    2750: "Ballerup"
}

print(postnumre.keys())
print(postnumre.values())
print(postnumre.items())

postnumre.update({2830:"Virum",2840:"Virum-Sorgenfri"})
print(postnumre.get(2830))
#Car-list
