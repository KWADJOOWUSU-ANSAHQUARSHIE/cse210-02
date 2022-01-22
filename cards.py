import random


class Cards:

    def __init__(self):
        self.draw = 0

    def draw_card(self):
        self.draw = random.randint(1, 13)
