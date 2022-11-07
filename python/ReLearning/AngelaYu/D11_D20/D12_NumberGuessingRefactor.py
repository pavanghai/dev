from random import randint
from sys import exit
from D12_NumberGuessingArt import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty_level():
    """setup the difficulty level based on user input"""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_LEVEL_TURNS
    elif level == 'hard':
        return HARD_LEVEL_TURNS
    else:
        exit("invalid input, exiting Guess Number Game...")

def check_answer(answer, guess, turns):
    """Checks the answer against the guess. 
    Returns the number of turns remaining."""  
    if guess == answer:
        print(f"You got it! The answer was {answer}.")
    else:
        if guess > answer:
            print("Too high.")
        else:
            print("Too low.")
        turns -= 1
    return turns

def game():
    print(logo)
    print("\nWelcome to the Number Gussing Game!\n"
          "I'm thinking of a number between 1 and 100.")
    
    answer = randint(1, 100)
    print(f"Guessed number: {answer}")
    turns = set_difficulty_level()
    
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        turns = check_answer(answer, guess, turns)
        
        if turns == 0:
            print("You've run out of guesses, you lose. ")
            return
        elif guess != answer:
            print("Guess again.")          

    print("Game over")

game()
