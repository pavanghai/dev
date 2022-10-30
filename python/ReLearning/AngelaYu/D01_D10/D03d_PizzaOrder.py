# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total = 0
if size.lower() == 's':
    total += 15
elif size.lower() == 'm':
    total += 20
elif size.lower() == 'l':
    total += 25

if add_pepperoni.lower() == 'y':
    if size.lower() == 's':
        total += 2
    elif size.lower() in ('m', 'l'):
        total += 3
if extra_cheese.lower() == 'y':
    total += 1

print(f"Your final bill is: ${total}.")