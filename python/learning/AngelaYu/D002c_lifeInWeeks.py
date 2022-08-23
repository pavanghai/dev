# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age = int(age)
max_age = 90
years = max_age - age
months = 12 * years
weeks = 52 * years
days = 365 * years
print(f"You have {days} days, {weeks} weeks, and {months} months left.")