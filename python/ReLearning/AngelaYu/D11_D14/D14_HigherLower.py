from os import name, system
from random import choice
from D14_HigherLowerArt import logo, vs
from D14_HigherLowerData import data


def format_name(person:dict) -> str:
    return (f"{person['name']}, a {person['description']}, "
            f"from {person['country']}.")

def check_result(answer, person_a, person_b):
    if answer == 'a' and person_a['follower_count'] > person_b['follower_count']:
        return True
    elif answer == 'b' and person_b['follower_count'] > person_a['follower_count']:
        return True
    else:
        return False

def switch_user(person_a, person_b):
    person_a = person_b
    person_b = choice(data)
    while person_a == person_b:
        person_b = choice(data)
    return person_a, person_b

def wrong_answer(score_count):
    system('cls' if name in ('nt', 'dos') else 'clear')
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score_count}")

def winners(person_a, person_b, score_count):
    system('cls' if name in ('nt', 'dos') else 'clear')
    print(logo)
    print(f"You're right! Current score: {score_count}")
    print(f"Compare A: {format_name(person_a)}")
    print(vs)
    print(f"Against B: {format_name(person_b)}")
    print(person_a['name'],person_a['follower_count'], person_b['name'],person_b['follower_count'], score_count)
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    correct_answer = check_result(answer, person_a, person_b)
    return correct_answer

score_count = 0
person_a = choice(data)
person_b = choice(data)
while person_a == person_b:
    person_b = choice(data)

print(logo)
print(f"Compare A: {format_name(person_a)}")
print(vs)
print(f"Against B: {format_name(person_b)}")
print(person_a['name'],person_a['follower_count'], person_b['name'],person_b['follower_count'], score_count)
answer = input("Who has more followers? Type 'A' or 'B': ").lower()
correct_answer = check_result(answer, person_a, person_b)
if not correct_answer:
    wrong_answer(score_count)

while correct_answer:
    score_count += 1
    person_a, person_b = switch_user(person_a, person_b)
    correct_answer = winners(person_a, person_b, score_count)
    if not correct_answer:
        wrong_answer(score_count)


# if answer == 'a' and person_a['follower_count'] > person_b['follower_count']:
#     score_count += 1
# elif answer == 'b' and person_b['follower_count'] > person_a['follower_count']:
#     score_count += 1



# start of the game
# logo higher lower
# text : Compare A: {name}, a {description}, from {country}.
# logo vs
# text : Against B: {name}, a {description}, from {country}.
# text Prompt : Who has more followers? Type 'A' or 'B': 

# works in loop till correct answer, some changes as below and so on
#       Score is increased
#       Against B BECOMES : Compare A:
# if correct answer 
# logo higher lower
# text : You're right! Current score: {score_count}
# text : Compare A: {name}, a {description}, from {country}.
# logo vs
# text : Against B: {name}, a {description}, from {country}.
# text Prompt : Who has more followers? Type 'A' or 'B': 

# if wrong answer 
# logo higher lower
# text : Sorry, that's wrong. Final score: {score_count}


# system('cls' if name in ('nt', 'dos') else 'clear')