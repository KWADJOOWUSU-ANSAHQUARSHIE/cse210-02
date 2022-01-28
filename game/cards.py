import random


class Cards:
    """A hand of cards with the numbers 1-13.

    The responsability of the cards is to randomly draw a card from the range
    of 1 to 13.

    Attributes:
        draw (int): any card within the range of 1 to 13
    """

    def __init__(self):
        """Constructs new Cards.

        Args:
            self (Cards): an instance of Cards.
        """
        self.draw = 0 

    def draw_card(self):
        """Changes the value of the card. The value of the new card won't be
        the same as the last one. 

        Args:
            self (Cards): an instance of Cards.
        """
        pseudo_draw = random.randint(1, 13)
        while pseudo_draw == self.draw:
            pseudo_draw = random.randint(1, 13)
        self.draw = pseudo_draw
