import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+','@','/']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#EASY METHOD
passcode=""
for char1 in range(1,nr_letters+1):
    passcode+=random.choice(letters)
for num1 in range(1,nr_numbers+1):
    passcode+=random.choice(numbers)
for symbol1 in range(1,nr_symbols+1):
    passcode+=random.choice(symbols)
print(f"YOUR PASSWORD IS READY TO USE: {passcode}")

print()
print()

#HARD METHOD
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password=[]
for char2 in range(0,nr_letters):
    password.append(random.choice(letters))
for num2 in range(0,nr_numbers):
    password.append(random.choice(numbers))
for symbol2 in range(0,nr_symbols):
    password.append(random.choice(symbols))
print(password)
random.shuffle(password)
print(password)

final_password=""
for chars in password:
    final_password+=chars
print(f"YOUR PASSWORD IS READY TO USE: {final_password}")

