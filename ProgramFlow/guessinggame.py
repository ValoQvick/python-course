answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess == answer:
    print("Hey, you got it! :)")
else:
    if guess < answer:
        print("Please guess higher: ")
    else:   # guess must be greater than answer
        print("Please guess lower: ")
    guess = int(input())
    if guess == answer:
        print("Well done! :)")
    else:
        print("Sorry, not correct. :(")

# if guess < answer:
#     print("Please guess higher: ")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it!")
#     else:
#         print("Sorry :(")
# elif guess > answer:
#     print("Please guess lower: ")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it!")
#     else:
#         print("Sorry :(")
# else:
#     print("Correct! :)")
