def multiply(a, b):
    result = a * b
    return result


def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1] == string


word = input("Please enter a word to check: ")
if is_palindrome(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))
