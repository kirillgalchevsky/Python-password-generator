import random
chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"

numbers = int(input("Number of password?:"))
length = int(input("Length of password: "))

for p in range(numbers):
    password = ""
    for c in range(length):
        password += random.choice(chars)
    print(password)