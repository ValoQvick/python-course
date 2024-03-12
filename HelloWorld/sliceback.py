#          01234567890123456789012345
letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[::-1]
print(backwards)

print(letters[16:13:-1])    # qpo
print(letters[4::-1])       # edcba
print(letters[:17:-1])      # last 8 characters in reverse order

print(letters[-4:])
print(letters[-1:])
print(letters[:1])
print(letters[0])   # might cause errors when empty
