# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names = name1.casefold()+name2.casefold()
TRUE, LOVE = "true", "love"
true_total, love_total = 0, 0
  
for t in TRUE:
    # print(f"{t} occures {NAMES.count(t)} time")
    true_total += names.count(t)
# print()
for l in LOVE:
    # print(f"{l} occures {NAMES.count(l)} time")
    love_total += names.count(l)

score = int(str(true_total) + str(love_total))
# print(score)
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")