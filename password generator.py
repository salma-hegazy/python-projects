import random

letters = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h',
           'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p',
           'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x',
           'Y', 'y', 'Z', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=',
           '{', '[', '}', ']', '|', '\\', ':', ';', '"', '<', '>', '.', '?', '/']

while True:
    try:
        num_letters = int(input("Please enter the number of letters you want in your password: "))
        num_numbers = int(input("Please enter the number of numbers you want in your password: "))
        num_symbols = int(input("Please enter the number of symbols you want in your password: "))
        break
    except ValueError:
        print(" Invalid input! Please enter a valid number.")

random_letters = random.sample(letters, num_letters)
random_numbers = random.sample(numbers, num_numbers)
random_symbols = random.sample(symbols, num_symbols)

password_list = random_letters + random_numbers + random_symbols

random.shuffle(password_list)

password = "".join(password_list)

print(f" Your random password is: {password}")