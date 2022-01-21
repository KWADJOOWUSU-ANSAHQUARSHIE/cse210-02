from cards import Cards


class Player:

    def __init__(self):
        # The score.
        self.score = 300
        # Will the player continue playing?
        self.is_playing = True
        # Variable for guessing higher or lower.
        self.guess = ''

        # Make an instance of the class Cards so we can use it whenever we want.
        self.cards = Cards()

        # Two different variables we can use to draw cards using the instance created above.
        # We draw current first and then we draw next to compare.
        self.current = None
        self.next = None

    def start_game(self):
        # Call the first_guess function, then write the while loop.
        pass

    def first_guess(self):
        # Use this function to draw and display the first current card and ask the user for the guess.

        # This function goes outside the while loop.
        # The reason being is that later we need to make self.current = self.next and after that
        # we change self.next to a new card. If we define the first self.current inside the while
        # loop, the self.current = self.next will be overwritten every time the while loop starts again.
        pass

    def make_guess(self):
        # Use this function to display the current card and ask the user for the guess.
        # This function goes inside the while loop.
        pass

    def check_guess(self):
        # Draw a card for self.next and check if the guess is correct or not.
        pass

    def display_output(self):
        # Display the score after the guess and if score < 0, self.is_playing = False to end game.
        # If game continues, make the change self.current = self.next.
        # Then, draw a new card in self.next.
        pass

    def keep_playing(self):
        # Ask user if they want to continue playing.
        # Depending of the answer, change self.is_playing to False to end loop.
        pass
