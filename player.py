from cards import Cards

class Player:
    def __init__(self):
        self.is_playing = True
        self.current_card = 0
        self.next_card = 0
        self.score = 300

        # deal = Cards()

    def start_game(self):
        while self.is_playing:
            self.high_or_low()
            self.update_score()
            self.results()

    def high_or_low(self):

        self.guess = input("Will the next card be higher or lower? \nPlease enter 'H' or 'L'")
        return self.guess
        
    def update_score(self):

        if self.guess.capitalize == Cards.result:
            self.score =+ 100
        else:
            self.score =+ -75
        
    def results(self):
        
        updated_results = 0
        print(updated_results)