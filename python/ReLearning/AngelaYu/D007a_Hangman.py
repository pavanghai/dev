from random import choice
from D007a_Hangman_art import stages, logo

"""
Flow Chart: https://drive.google.com/file/d/1jD5Gw6nSx-dpMhHhUHqsWOkHzOOT7iGG/view?usp=sharing   
"""

FRUITS = ('apples', 'orange', 'mango', 'pear',
                'peache', 'apricot', 'grapes', 'kiwi',
                'watermelon', 'banana')
# print(logo)
fruit = "banana".upper() # TODO: replace with choice method --> choice(FRUITS).upper()
fruit_length = len(fruit)
fruit_line = list('_' * fruit_length)

print(f"{fruit} - length {fruit_length}")
print(f"guess the fruit name {fruit_line}\n")
print(f"{fruit_line}\n") # TODO: convert to string with space in between, this is just for display

game_over = False
life_count = len(stages) - 1

while not game_over:
    # TODO: print the blank lines of the word 
    guess_char = input("Guess a letter: ").upper()
    if guess_char in fruit:
        for i in range(len(fruit)):
            if fruit[i] == guess_char:
                fruit_line[i] = guess_char
        print(f"After {fruit_line}")
        if "_" not in fruit_line:
            print("You win...")
            game_over = True
    else:
        print(f"You guessed {guess_char}, that's not in the word. You lose a life.")
        print(stages[life_count])
        if life_count > 0:
            life_count -= 1
        else:
            print("You lost the game...")
            game_over = True

# if guess_char in fruit:
#     print(guess_char)
#     guess_char_index = fruit.find(guess_char)

# for s in reversed(stages):
#     print(s)