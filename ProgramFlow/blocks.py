name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

if age <= 18:
    print("You are underage and therefore not allowed to buy alcoholic beverages.")
else:
    print("You are allowed to buy alcoholic beverages.")
