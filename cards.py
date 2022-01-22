import random

# To make things simpler, the Cards class just draws a random card.
# We can make two variables in Player called current and next using the
# the same Cards class.


class Cards:

    def __init__(self):
        self.draw = 0

    def draw_card(self):
        self.draw = random.randint(1, 13)
