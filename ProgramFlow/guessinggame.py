import random

highest = 10
answer = random.randint(1, highest)
print(answer)   #TODO: Remove after testing

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())

while guess != answer:
    if guess == 0:
        print("You quit the game.")
        break
    elif guess < answer:
        print("Please guess higher: ")
    elif guess > answer:   # guess must be greater than answer
        print("Please guess lower: ")
    guess = int(input())

print("Hey, you got it! :)")

# if guess == answer:
#     print("Hey, you got it! :)")
# else:
#     if guess < answer:
#         print("Please guess higher: ")
#     else:   # guess must be greater than answer
#         print("Please guess lower: ")
#     guess = int(input())
#     if guess == answer:
#         print("Well done! :)")
#     else:
#         print("Sorry, you have not guessed correctly. :(")
