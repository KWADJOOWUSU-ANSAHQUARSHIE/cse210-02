import random

class Cards:

    def __init__(self):
        self.current_card = 0
        self.next_card = 0

    def card(self):
        """Card will choose a random number from 1-13."""
        self.card_number1 = random.randint(1, 13)
        
    
    def highpoints(self):
        """Points will adjust based comparison to the current card"""
        if self.next_card > self.current_card:
            return +100
        elif self.next_card < self.current_card:
            return -75


    def lowpoints(self):
        """Points will adjust based comparison to the current card"""
        if self.next_card < self.current_card:
            return self.pointstotal + 100
        elif self.next_card > self.current_card:
            return self.pointstotal - 75