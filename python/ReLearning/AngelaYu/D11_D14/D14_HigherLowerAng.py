from os import name, system
from random import choice
from D14_HigherLowerArt import logo, vs
from D14_HigherLowerData import data

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_descr}, from {account_country}.")

def check_answer(guess, a_follower, b_follower):
    """Takes the user guess and follower counts and returns if they got it right."""
    # Ternary operator for if condition
    # return guess == 'a' if a_follower > b_follower else guess == 'b'
    if a_follower > b_follower:
        return guess == 'a'
    else:
        return guess == 'b'
    
# Display art
print(logo)
score = 0
game_should_continue = True
# Generate a random account from the game data.
account_b = choice(data)
# Make the game repeatable.
while game_should_continue:
    # Generate a random account from the game data. (used before loop for b)

    # Making account at position B become the next account at position A.
    account_a = account_b
    account_b = choice(data)

    while account_a == account_b:
        account_b = choice(data)

    # Format the account data into printable format.
    ##### Converted to function as using again for other account too.. # format_data(account):
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    '''  'name': 'Ariana Grande',  'follower_count': 183, 'description': 'Musician and actress', 'country': 'United States' '''
    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct. # Create a function as this count repete too check_answer(guess, a_follower, b_follower):
    ## Get follower count of each account.
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    ## Use if statement to check if user is correct.
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear the screen between rounds.
    system('cls' if name in ('nt', 'dos') else 'clear')
    print(logo)

    # Give user feedback on their guess.
    # Score keeping.
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")