class Wolf:
    def __init__(self, legs):
        self.legs = 4

    def walk(self):
        print("walkies")

    def make_noise(self):
        print("howl")

class Dog(Wolf):
    def __init__(self, legs, color):
        super().__init__(legs)
        self.color = color

    def make_noise(self):
        print("woof")

class Lead():
    def __init__