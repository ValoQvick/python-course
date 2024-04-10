def multiply(a, b):
    result = a * b
    return result


answer = multiply(10.5, 4)
print("Answer is: ", answer)

forty_two = multiply(6, 7)
print("Answer is: ", forty_two)

print()

for val in range(1, 5):
    two_times = multiply(2, val)
    print(two_times)
