from cardset import CardSet


class Game:

    def __init__(self):
        deck = CardSet()
        deck.new_deck()
        self.deck = deck
        user_set = CardSet()
        self.user_set = user_set
        james_set = CardSet()
        self.james_set = james_set
        self.result = None

    @staticmethod
    def decision():
        while True:
            answer = input()
            if answer.upper() not in ['Y', 'N']:
                print('I do not understand. Repeat please... (y/n)')
                continue
            return True if answer in ['Y', 'y'] else False

    def user_turn(self):
        self.user_set.set_of_cards = []
        self.user_set.take_card(self.deck)
        self.user_set.take_card(self.deck)
        print(self.user_set)
        u_score = self.user_set.score
        print(f'Your Score: {u_score}.\nHit another? (y/n)')
        while self.decision():
            self.user_set.take_card(self.deck)
            print(self.user_set)
            u_score = self.user_set.score
            if u_score > 21:
                print(f'Your score: {u_score}.\nToo much! You have lost...\n')
                self.result = False
                return False
            print(f'Your score: {u_score}.\nHit another? (y/n)')
        return True

    def james_turn(self):
        self.james_set.set_of_cards = []
        self.james_set.take_card(self.deck)
        self.james_set.take_card(self.deck)
        print(self.james_set)
        j_score = self.james_set.score
        print(f'My score: {j_score}. ', end='')
        while j_score < self.user_set.score and j_score < 21:
            print('I\'ll take another...')
            self.james_set.take_card(self.deck)
            print(self.james_set)
            j_score = self.james_set.score
            print(f'My score: {j_score}.')

    def check(self):

        if self.james_set.score > 21:
            print('Damn! I have lost...\n')
            self.result = True
        elif self.james_set.score >= self.user_set.score:
            print('I win!\n')
            self.result = False
