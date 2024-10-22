# is_hot = True
# is_cold = False
# if is_hot :
#     print("It's a hot day")
#     print("Drink plenty of water")

# elif is_cold:
#     print("It's a cold day")
#     print("Wear  warm clothes")
    
# else:
#     print("It's a lovely day")
    
# print ("Enjoy your day")

# price = 10000000
# has_good_credit = True

# if has_good_credit:
#     down_payment = 0.1*price

# else:
#     down_payment = 0.2*price

# print(f"Down payment: $ {down_payment}")

# has_high_income = True
# has_good_credit = False

# if has_high_income or has_good_credit:
#     print("Eligible for  loan")
# temperature = 35
# if temperature != 30:
#     print("It's a hot day")

# else:
#     print("It's not a hot day")


# name = "Zipporah Kavutha Mutua"
# if len(name) < 3:
#     print("name must be at least 3 characters")

# elif len(name) > 50:
#     print("name must be a maximum of 50 characters")

# else:
#     print("name looks good")

# weight = int(input("Weight: "))
# unit = input("(L)bs or (K)g: ")
# if unit.upper() == "L":
#     weight = weight*0.45
#     print(f"You are {weight} kilos")

# else:
#     weight = weight/0.45
#     print(f"You are {weight} pounds")

# i = 1
# while i <= 5:
#     print(i)
#     i += 1
    
# print("Done")
# secret_number = 5
# guess_count = 0
# guess_limit = 3

# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count  += 1
#     if guess == secret_number:
#         print("You won")
#         break
# else:
#     print("You failed")

# print("    Game Done!")

# command  = ""
# started = False
# while True:
#     command = input(">").lower()
#     if command == "start":
#         if started:
#            print("Car has already started...")
#         else:
#             started = True
#             print("Car started...")
            
#     elif command == "stop":
#         if not started:
#             print("The car has already stopped")
#         else:
#             started = False
#             print("Car stopped")
#     elif command == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit- to quit
#         """)
#     elif command == "quit":
#         break

#     else:
#         print("Sorry I don't understand the command")


# prices = [10,20,30]
# total = 0
# for price in prices:
#     print(f"price: {price}")
#     total += price
# print( f"total=  {total}")
# for x in range(2):
#     for y in range (1):
#         for z in range (2):
#              print(f"({x}, {y} , {z})")
# numbers = [5, 2, 5, 2, 2]
# for L_count  in numbers:
#     output = ""
#     for count in range(L_count):
#         output += "L"
#     print(output)
    
# numbers = [1, 2,3,56,89,2,3,15,0,667,23,23,2,1]
# max = numbers[7]
# for number in numbers:
#     if number < max:
#         max=number

# print(max)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for column in matrix:
#     for item in column:
#         print(item)


# numbers = [3,4,8,3,4,7,9,5,4,7,3,48,5]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number) 
        
# print(uniques)


# coordinates = (1,2,3)
# x, y, z = coordinates
# print(y)

# phone = input("phone: ")
# digits_mapping = {"0": "Zero",
#                   "1": "One", 
#                   "2": "Two",
#                   "3": "Three", 
#                   "4": "Four", 
#                   "5": "Five", 
#                   "6": "Six", 
#                   "7": "Seven",
#                   "8": "Eight", 
#                   "9": "Nine"}
# output = " "
# for character in phone:
#     output += digits_mapping.get(character,  "!") + " "

# print(output)
# message = input(">")
# words = message.split(' ')
# emojis = {
# ":)": "😆",
# ":(": "😔"
    
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
    
# print(output)
# def square(number):
#     return number*number

# result = square(3)
# print(result)

# def emoji_converter(message):
#     words = message.split(' ')
#     emojis = {
#     ":)": "😆",
#     ":(": "😔"
        
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output


# message =  input(">")
# print(emoji_converter(message))

# try:
#     age = int(input("Age: "))
#     income = 2000
#     risk = income/age
#     print(age)
# except ZeroDivisionError:
#     print("division by zero")
# except ValueError:
#     print("Invalid value")
# try:
#     age = int(input("Age: "))
#     income = 2000
#     risk = income/age
#     print(age)
# except ZeroDivisionError:
#     print("division by zero")
# except ValueError:
#     print("Invalid value")
# class Point:
#     def move(self):
#         print("move")

#     def draw(self):
#         print("draw")

# point1  = Point()
# point1.x = 10
# point1.y = 20
# print(point1.y)
# point1.draw()

# point2 = Point()
# point2.x = 3
# point2.y = 5
# print(point2.x)
# point2.move()
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def move(self):
#         print("move")

#     def draw(self):
#         print("draw")

# point1  = Point(10,20)
# point1.x = 17
# print(point1.x)
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         print(f"Hi, I am {self.name}")
# name = Person("Zippy Mutua")
# name.talk()

# bob = Person("Bob Smith")
# bob.talk()
# class Mammal:
#     def walk(self):
#         print("walk")


# class Dog(Mammal):
#     def bark(self):
#         print("bark")

# class Cat(Mammal):
#     def be_annoying(self):
#         print("annoying")
        





# dog1 = Dog()
# dog1.bark()

# cat1 = Cat()
# cat1.be_annoying()

# import converters
# weight = 


# from utils import find_max

# numbers = [1, 2,3,56,89,2,3,15,0,667,23,23,2,1]
# maximum = find_max(numbers)
# print(maximum)

# from ecommerce import shipping

# shipping.calc_shipping()
# shipping.calc_shipping()

import random

for i in range(3):
    print(random.randint(10,20))


