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
        self.card = Cards()

        # Two different variables we can use to draw cards using the instance created above.
        # We draw current first and then we draw next to compare.
        self.current = None
        self.next = None

    def start_game(self):
        # Call the first_guess function, then write the while loop.
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
        # Use this function to draw and display the first current card and ask the user for the guess.

        # This function goes outside the while loop.
        # The reason being is that later we need to make self.current = self.next and after that
        # we change self.next to a new card. If we define the first self.current inside the while
        # loop, the self.current = self.next will be overwritten every time the while loop starts again.
        print()
        print("Welcome player!\n")
        print("Your current score is 300 points.")
        print("Based on your guess you will lose points or earn points.")
        print("If the card is the same, you will automatically earn 100 points.")
        print("When you reach 0, the game will be over.\n")

        self.card.draw_card()
        self.current = self.card.draw

        print(f"You are holding a {self.current}.")
        self.guess = input("Will the next card be higher or lower? (h/l): ")

    def make_guess(self):
        # Use this function to display the current card and ask the user for the guess.
        # This function goes inside the while loop.
        print(f"You are holding a {self.current}.")
        self.guess = input("Will the next card be higher or lower? (h/l): ")

    def check_guess(self):
        # Draw a card for self.next and check if the guess is correct or not.
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
        # Display the score after the guess and if score < 0, self.is_playing = False to end game.
        # If game continues, make the change self.current = self.next.
        # Then, draw a new card in self.next.
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
        # Depending of the answer, change self.is_playing to False to end loop.
        play_more = input("Would you like to keep playing? [yes/no] ")

        if play_more == "yes":
            print()
        elif play_more == "no":
            print("\nThanks for Playing :)\n")
            self.is_playing = False
        else:
            print()
            print("Entered an invalid input.\nThe game is over.")
            print("Follow the rules next time >:(\n")
            self.is_playing = False
