from random import randint
from sys import exit
from D12_NumberGuessingArt import logo

answer = randint(1, 100)
game_continue = True
# print(f"Guessed number: {answer}")

print(logo)
print("\nWelcome to the Number Gussing Game!\n"
      "I'm thinking of a number between 1 and 100.")

level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if level == 'easy':
    guess_attempt = 10
elif level == 'hard':
    guess_attempt = 5
else:
    exit("invalid input, exiting Guess Number Game...")

while game_continue and guess_attempt > 0:
    print(f"You have {guess_attempt} attempts remaining to guess the number")
    user_guessed = int(input("Make a guess: "))
    if user_guessed == answer:
        print("you guessed it correct...")
        game_continue = False
    else:
        if user_guessed > answer:
            print("Too high.")
        else:
            print("Too low.")

        if guess_attempt != 1:
            print("Guess again.")
        guess_attempt -= 1

print("Game over")

# TODO: refacor code to make it as functions (use def) use global variable Global Constant 
