import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
    'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 
    'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
eazy_password = "".join(random.choices(letters, k=nr_letters) \
    + random.choices(symbols, k=nr_symbols) \
    + random.choices(numbers, k=nr_numbers))
print("Easy Password: ", eazy_password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hard_password = random.choices(letters, k=nr_letters) \
    + random.choices(symbols, k=nr_symbols) \
    + random.choices(numbers, k=nr_numbers)

# print(hard_password, type(hard_password))
random.shuffle(hard_password)
# print(hard_password, type(hard_password))
hard_password = "".join(hard_password)
print("Hard Password: ", hard_password)

# I want to have something like this but I am getting TypeError: can only join an iterable
# hard_password = "".join(random.shuffle([random.choices(letters, k=nr_letters) \
#     + random.choices(symbols, k=nr_symbols) \
#     + random.choices(numbers, k=nr_numbers)]))

# How do I make above code to work?
# If ignore join, get None value from random.shuffle
# hard_password = random.shuffle([random.choices(letters, k=nr_letters) \
#     + random.choices(symbols, k=nr_symbols) \
#     + random.choices(numbers, k=nr_numbers)])
# print(hard_password, type(hard_password))
