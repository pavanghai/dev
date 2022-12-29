class Animal:

    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print("Inhale, exhale")


class Fish(Animal): # Inheritance from Animal class

    def __init__(self):
        super().__init__() # initializing from super class

    def breath(self):
        super().breath() # executing method from super(parent) class can use below command too
        # Animal().breath()  # executing method from super(parent) class
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.swim()
nemo.breath()
print(nemo.num_eyes)