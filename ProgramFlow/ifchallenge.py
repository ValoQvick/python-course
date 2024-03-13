print("Welcome to the Holiday Lounge!\nPlease remember that we do have age restriction.")
# age restriction 18-30

name = input("Enter your name, please: ")
age = int(input("Enter your age, please: "))

if 18 <= age < 31:
    print("Welcome and please enjoy your stay, {}!".format(name))
else:
    print("I'm sorry, but you are not within the age restriction. Have a good day.")
