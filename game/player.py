from game.cards import Cards


class Player:
    """The player of the game.

    The responsabilities of the player is to guess if the next card will be
    higher or lower than the current one and to keep track of the score.

    Attributes:
        score (int): the score of the player
        is_playing (boolean):  whether or not the game is being played
        guess (string): the guess of the player
        card (Cards()): a Cards instance
        current (int): the current card displayed
        next (int): the next card to draw
    """

    def __init__(self):
        """Constructs a new Player.

        Args:
            self (Player): an instance of Player.
        """
        self.score = 300
        self.is_playing = True
        self.guess = ''

        self.card = Cards()

        self.current = None
        self.next = None

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Player): an instance of Player.
        """
        self.first_guess()
        while self.is_playing:
            self.check_guess()

            if self.is_playing:
                self.display_output()

                if self.is_playing:
                    self.keep_playing()

                    if self.is_playing:
                        self.make_guess()

    def first_guess(self):
        """Introduce the game, draw the first card, display the first card,
        and make the first guess.

        Args:
            self (Player): an instance of Player.
        """
        print()
        print("Welcome player!\n")
        print("Your current score is 300 points.")
        print("Based on your guess you will lose points or earn points.")
        print("When you reach 0, the game will be over.\n")

        self.current = self.card.draw

        print(f"You are holding a {self.current}.")
        self.guess = input("Will the next card be higher or lower? (h/l): ")

    def make_guess(self):
        """Display the current card and make a guess.

        Args:
            self (Player): an instance of Player.
        """
        print(f"You are holding a {self.current}.")
        self.guess = input("Will the next card be higher or lower? (h/l): ")

    def check_guess(self):
        """Draw the next card, check if the guess is correct, and change the score.

        Args:
            self (Player): an instance of Player.
        """
        self.card.draw_card()
        self.next = self.card.draw

        if self.guess == "h":
            if self.current > self.next:
                self.score -= 75
            else:
                self.score += 100

        elif self.guess == "l":
            if self.current < self.next:
                self.score -= 75
            else:
                self.score += 100

        else:
            print()
            print("Entered an invalid input.\nThe game is over.")
            print("Follow the rules next time >:(\n")
            self.is_playing = False

    def display_output(self):
        """Display the results of the guess. End the game if the score is 0.

        Args:
            self (Player): an instance of Player.
        """
        print(f"The next card was a {self.next}.")

        if self.score <= 0:
            print(f"Your current score is {self.score}.\n")
            print("Sorry! you lost.\nTry again next time.\n")
            self.is_playing = False

        else:
            print(f"Your current score is {self.score}")

            self.current = self.next
            self.card.draw_card()
            self.next = self.card.draw

    def keep_playing(self):
        """Ask the user if the player if they want to keep playing.

        Args:
            self (Player): an instance of Player.
        """
        play_more = input("Would you like to keep playing? [yes/no] ")

        if play_more.capitalize() == "Y" or play_more.capitalize() == "Yes":
            print()
        elif play_more.capitalize() == "N" or play_more.capitalize() == "NO":
            print("\nThanks for Playing :)\n")
            self.is_playing = False
        else:
            print()
            print("Entered an invalid input.\nThe game is over.")
            print("Follow the rules next time >:(\n")
            self.is_playing = False
