# Answer 1
# age = int(input())
# if age < 13:
#     print("Child")
# elif age < 20:
#     print("Teenager")
# elif age < 60:
#     print("Adult")
# else:
#     print("Senior")

# Answer 2
# age = int(input('enter age:'))
# days = "Wednesday"
# price = 12 if age >= 18 else 8

# if days == "Wednesday":
#     price -= 2
# print("Ticket price: $", price)

# Answer 3
score = int(input("enter score:"))

if score >= 101:
    print("Please enter a valid score")
    exit()

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# Answer 4
fruit = "Banana"
color = "Yellow"

# if fruit == "Banana":
#     if color == "Yellow":
#         print("Ripe")
#     elif color == "Green":
#         print("Unripe")
#     elif color == "Brown":
#         print("OverRipe")

# Answer 5
weather = "Sunny"

if weather == "Sunny":
    activity = "Go for a walk"
elif weather == "Rainy":
    activity = "Read a book"    
elif weather == "Snowy":
    activity = "Build a snowman"
print(activity)
    

# Answer 6
distance = 10

if distance < 3:
    transport = "Walk"
elif distance < 15:
    transport = "Bike"
else:
    transport = "Car"
print(transport)


# Answer 7
order_size = "Medium"
extra_shot = True

if extra_shot:
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee"

print("coffee: ", coffee)

# Answer 8
password = "password"

if len(password) < 6:
    print("Password is too short")
elif len(password) > 12:
    print("Password is too long")
else:
    print("Password is just right")

# Answer 9
year = 2020

if (year % 4 == 0 and year % 100 != 0 )or (year % 400 == 0):
    print(year,"Leap year")
else:
    print(year,"Not a leap year")


# Answer 10
pet_type = "Dog"
pet_age = 5

if pet_type == "Dog":
    if pet_age < 2:
        print("Puppy")
    else:
        print("Adult")

if pet_type == "Cat":
    if pet_age > 5:
        print("Senior cat food")
    else:
        print("Regular cat food")
    

