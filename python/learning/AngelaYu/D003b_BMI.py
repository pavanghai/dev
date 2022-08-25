# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
'''
Instructions
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
It should tell them the interpretation of their BMI based on the BMI value.
Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.
'''
bmi = int(round(weight/height**2,0))
msgs = ("are underweight", "have a normal weight", "are slightly overweight", "are obese", "are clinically obese.")
msg = ""
if bmi > 18.5 and bmi < 25:
    msg = msgs[1]
elif bmi > 25 and bmi < 30:
    msg = msgs[2]
elif bmi > 30 and bmi < 35:
    msg = msgs[3]
elif bmi > 35:
    msg = msgs[4]
else:
    msg = msgs[0]

print(f"Your BMI is {bmi}, you {msg}.")