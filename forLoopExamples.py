
# If statements
# An if statement is used to compare things

# variable = input("This is an input that will take a response")
# print(variable)

# Going to ride the Coney Island roller coaster
# 4' aka 48''
# height = int(input("How tall are you in inches? "))
# if height >= 48:
#     print("You are tall enough to ride the roller coaster!")
# else:
#     print("Sorry, you are not tall enough to ride the roller coaster.")


    #create a password checker
    # username = HotDogWater123
    # password = bluepen

# password = "bluepen"

# userLoginInput = input("Enter Password: ")

# if userLoginInput == password:
#     print("Open Sesame")
# else:
#     print("Access denied!")

#update if statement to while loop so that user can have multiple attempts
# while userLoginInput != password:
#     print("Wrong password - please try again")
#     userLoginInput = input("Enter Password:")

# print("Open Sesame")
          

# #check if number is even or odd:
# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print("Even!")
# else:
#     print("Odd!")


# Write a for loop for the value 1-152
# for number in range(1, 153) :
#     print(number)

# countdown from 10-0
#for number in range(10, 0, -1):
#     print(number)

# print("Blast off!")

# who likes root beer?
# numberOfRootBeers = 31

# for i in range( numberOfRootBeers, 1, -1):
#     print(f"{i} bottles of root beer on the wall....")
#     print(f"{i} bottles of root beer....")
#     print(f"{i} take one down, pass it around....")
#     print(f"{i-1} bottles of root beer on the wall....")

#  what is the sum of 1-427
# total = int(input("Pick a number to add up to: "))

# for number in range(1, 428):
#     total += number

# print(f"Your total is: {total}!")

# find the largest number
# numberList = [7, 42, 8, 946, -1, 4235, 6, 730]

# largestNumber = numberList[0]

# for number in numberList:
#     if number > largestNumber:
#         largestNumber = number

# print(largestNumber)

# Who wants to play... GUESS THAT NUMBER!
secretNumber = 7

guess = 0

while guess != secretNumber:
    guess = int(input("Guess the secret number: "))

print("You got it!")

