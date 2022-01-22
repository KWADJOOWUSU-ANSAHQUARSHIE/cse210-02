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
        card = Cards()

        # Two different variables we can use to draw cards using the instance created above.
        # We draw current first and then we draw next to compare.
        self.current = None
        self.next = None

    def start_game(self):
        # Call the first_guess function, then write the while loop.
        self.first_guess()
        while self.is_playing:
            self.make_guess()
            self.is_playing

    def first_guess(self):
        # Use this function to draw and display the first current card and ask the user for the guess.

        # This function goes outside the while loop.
        # The reason being is that later we need to make self.current = self.next and after that
        # we change self.next to a new card. If we define the first self.current inside the while
        # loop, the self.current = self.next will be overwritten every time the while loop starts again.
        print("Welcome player!")
        card = Cards()
        card.draw_card()
        self.current = card.draw
        print(f"You are holding a {self.current}")
        self.guess=input("Will the next card be higher or lower? (h/l): ")


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
        if self.score > 0:
            print(f"Your current score it {self.score}")
            self.current = self.next
            card = Cards()
            card.draw_card()
            self.next = card.draw

        elif self.score <= 0:
            self.is_playing = False
            print("Sorry you lost, try again next time")
            

    def keep_playing(self):
        
        # Depending of the answer, change self.is_playing to False to end loop.
        play_more = input("Would you like to keep playing (yes or no)?: ")
        if play_more == "yes":
            self.is_playing = True
        elif play_more == "no":
            self.is_playing = False
            print("Thanks for Playing :)")
