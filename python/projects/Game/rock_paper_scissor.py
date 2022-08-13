'''
       choice   rock   paper   scissors
         rock      0      -1          1
        paper      1       0         -1
      scissor     -1       1          0    
'''

rules = [
    [0, -1, 1],
    [1, 0, -1],
    [-1, 1, 0],
]
# rules[0][1] # Rock vs Paper = -1, Paper wins over Rock
class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""

    def choose(self):
        self.choice = input(
            f"{self.name}, select rock, paper or scissor: ")
        print(f"{self.name}, selects {self.choice}...")
    
    def to_numerical_choice(self):
        switcher = {"rock":0, "paper":1, "scissor":2}
        return switcher[self.choice]


class GameRound:
    def __init__(self, p1, p2):
        p1.choose()
        p2.choose()
    def compare_choices(self, p1, p2):
        print("implement")
        return self.rules[]
    def award_points(self):
        print("implement")


class Game:
    def __init__(self):
        self.end_game = False
        self.first_player = Participant("Spock")
        self.second_player = Participant("Kirk")
    def start(self):
        game_round = GameRound(self.first_player, self.second_player)
    def check_end_condition(self):
        print("implement")
    def determine_winner(self):
        print("implement")

game = Game()
game.start() 
    

