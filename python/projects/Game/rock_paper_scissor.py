# '''
#        choice   rock   paper   scissors      Example
#          rock      0      -1          1      Rock vs Paper = -1  Paper wins over Rock  Rock vs Scissors = 1 Rock wins over Scissors
#         paper      1       0         -1
#       scissor     -1       1          0    
# '''

# rules = [
#     [0, -1, 1],
#     [1, 0, -1],
#     [-1, 1, 0],
# ]
# # rules[0][1] # Rock vs Paper = -1, Paper wins over Rock
# class Participant:
#     def __init__(self, name):
#         self.name = name
#         self.points = 0
#         self.choice = ""

#     def choose(self):
#         self.choice = input(
#             f"{self.name}, select rock, paper or scissor: ")
#         print(f"{self.name}, selects {self.choice}...")
    
#     def to_numerical_choice(self):
#         switcher = {"rock":0, "paper":1, "scissor":2}
#         return switcher[self.choice]


# class GameRound:
#     def __init__(self, p1, p2):
#         p1.choose()
#         p2.choose()
#     def compare_choices(self, p1, p2):
#         print("implement")
#         return self.rules[]
#     def award_points(self):
#         print("implement")


# class Game:
#     def __init__(self):
#         self.end_game = False
#         self.first_player = Participant()
#         self.second_player = Participant()
#     def start(self):
#         game_round = GameRound(self.first_player, self.second_player)
#     def check_end_condition(self):
#         print("implement")
#     def determine_winner(self):
#         print("implement")

# game = Game()
# game.start() 
########################################################################################################################
# The rules of the game state that rock wins over scissors, scissors beats (cuts) paper, and paper beats (covers) rock. 
#        choice     rock   paper     scissors
#          rock      0      -1          1
#         paper      1       0         -1
#       scissor     -1       1          0  
#-----------------------------------------------------------------------------------------------------------------------
#   Phase         Actor         Behavior                                 Data
# 1 Input         Participant   Chooses symbol                           Symbol saved as choice on Participant(choice)
# 2 Processing    GameRound     Compares choices against game rules      Result inspected
# 3 Processing    GameRound     Awards points based on result value      Points added to winning Participant(point)
# 4 Processing    Game          Check continue answer                    Answer is true, continue, else quit
# 5 Output        Game          New game round or game end credit	
#-----------------------------------------------------------------------------------------------------------------------
#   Behavior                Method                Actor
# 1 Chooses symbol          choose()              Participant
# 2 Compares choices        compareChoices()      GameRound
# 3 Awards points           awardPoints()         GameRound
# 4 Check continue answer   checkEndCondition()   Game
# 5 Game end credit         determineWinner()     Game
#-----------------------------------------------------------------------------------------------------------------------

class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""
    def choose(self):
        self.choice = input("{name}, select rock, paper or scissor: ".format(name=self.name))
        print("{name} selects {choice}".format(name=self.name, choice=self.choice))
    def toNumericalChoice(self):
        switcher = {
            "rock": 0,
            "paper": 1,
            "scissor": 2
        }
        return switcher[self.choice]
    def incrementPoint(self):
        self.points += 1

class GameRound:
    def __init__(self, p1, p2):
        self.rules = [
            [0, -1, 1],
            [1, 0, -1],
            [-1, 1, 0]
        ]
        p1.choose()
        p2.choose()
        result = self.compareChoices(p1, p2)
        print("Round resulted in a {result}".format(result=self.getResultAsString(result)))
        if result > 0:
            p1.incrementPoint()
        elif result < 0:
            p2.incrementPoint()
    def compareChoices(self, p1, p2):
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]
    def awardPoints(self):
        print("implement")
    def getResultAsString(self, result):
        res = {
            0: "draw",
            1: "win",
            -1: "loss"
        }
        return res[result]

class Game:
    def __init__(self):
        self.endGame = False
        self.participant = Participant("Spock")
        self.secondParticipant = Participant("Kirk")
    def start(self):
        game_round = GameRound(self.participant, self.secondParticipant)
    def checkEndCondition(self):
        print("implement")
    def determineWinner(self):
        print("implement")

game = Game()
game.start()