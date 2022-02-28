#Print every name in list
names = ("Nicklas", "Benjamin", "Claus")

for name in names:
    print(name)

#Sum numbers 1-10
numbers = [1,2,3,4,5,6,7,8,9,10]
sum = 0

for number in numbers:
    sum += number

#For loop in Range
for i in range(1,6):
    print(i)

#Counting
counter = 0
for i in range(0,6):
    counter += 1


#Print every second number
for counter in range(0,10,2):
    print(counter)

#Print every second element
mail_list = ["nifr@kea.dk", 10, "behu@kea.dk", 12,"cbvi@kea.dk",15]

for element in mail_list[::2]:
    print(element)
