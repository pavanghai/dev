"""
This is the sample class created to check the effect of object calling another object
see follow method self refers to the object and user refers to the other object
"""


class User:

    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Some buddy")
user_2 = User("002", "No buddy")

user_1.follow(user_1)
print(f"User_1 following user_1: \n{user_1.__dict__}\n{user_2.__dict__}")
print(user_2.id, user_2.name, user_2.followers, user_2.following)
user_1.follow(user_2)
print(f"User_1 following user_2: \n{user_1.__dict__}\n{user_2.__dict__}")
