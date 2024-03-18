print("Please choose your option from the list below: ")
print("1:\tLearn Python")
print("2:\tPlay Stardew Valley")
print("3:\tGo hiking")
print("4:\tEat something")
print("5:\tTime to sleep")
print("0:\tExit")

while True:
    choice = input()

    if choice == "0":
        break
    elif choice in "12345":
        print("You chose {}".format(choice))
