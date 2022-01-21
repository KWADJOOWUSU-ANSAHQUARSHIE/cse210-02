import random

class Cards:
    def __init__(self):
        self.current_card = 0
        self.next_card = 0
        self.result = ""

    def card(self):
        self.current_card = random.randint(1,13)
        self.next_card = random.randint(1,13)
        
        if self.next_card > self.current_card:
            self.result = "H"

        else:
            self.result = "L"