from os import system, name
from random import choice
from time import sleep

from D007a_Hangman_art import stages, logo
from D007a_Hangman_word import word_list


word = choice(word_list).upper()
display_word = list('_' * len(word))
life_count = len(stages) - 1

wrong_guess = []
game_over, lost_life = False # Created switch

print(logo)
while not game_over:
    # print(f"{word} - length {len(word)}") # Use for testing
    print(f"{' '.join(display_word)}\n")
    if lost_life:
        print(stages[life_count])
    guess_char = input("Guess a letter: ").upper()
    
    if guess_char in word:
        for i in range(len(word)):
            if word[i] == guess_char:
                display_word[i] = guess_char
        if "_" not in display_word:
            print("You win...")
            game_over = True
    else:
        if life_count > 0:
            if guess_char not in wrong_guess:
                print(f"You guessed {guess_char}, that's not in the word. You lose a life.")
                life_count -= 1
                lost_life = True
            else:
                print(f"You already guessed {guess_char} try other letter")
            wrong_guess.append(guess_char)
        else:
            print("You lost the game...")
            game_over = True
    sleep(2)
    system('cls' if name in ('nt', 'dos') else 'clear')