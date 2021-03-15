from cardset import CardSet
from user import User


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
        player = User('')
        self.player = player
        self.pot = 0

    def start(self):
        print('#### BLACK JACK ####')
        print('Hi! My name is James. What is your name?')
        u_name = input()
        self.player = User(u_name)
        print(f'Nice to meet you {self.player.name}.\nWanna play Black Jack? Cash in is 1000$ (y/n)')

    def bet(self):
        print('How much you wanna bet?')
        while True:
            answer = input()
            if answer.isdigit():
                if int(answer) > self.player.cash:
                    print('Nice try. You do not have such money! Try again...')
                else:
                    self.pot = int(answer)
                    break
            else:
                print('Wrong number... try again.')

    @staticmethod
    def decision():
        while True:
            answer = input()
            if answer.upper() not in ['Y', 'N']:
                print('I do not understand. Repeat please... (y/n)')
                continue
            return True if answer in ['Y', 'y'] else False

    def user_hit(self):
        self.user_set.take_card(self.deck)
        if len(self.deck) == 0:
            print('Last card from the deck taken. Cards shuffled, new deck introduced.')
            self.deck.new_deck()

    def james_hit(self):
        self.james_set.take_card(self.deck)
        if len(self.deck) == 0:
            print('Last card from the deck taken. Cards shuffled, new deck introduced.')
            self.deck.new_deck()

    def user_turn(self):
        self.user_set.set_of_cards = []
        self.user_hit()
        self.user_hit()
        print(f'Pot: {self.pot}$')
        print(f'Your cards: {self.user_set}')
        u_score = self.user_set.score
        print(f'Your Score: {u_score}.\nHit another? (y/n)')
        while self.decision():
            self.user_hit()
            print(self.user_set)
            u_score = self.user_set.score
            if u_score > 21:
                print(f'Your score: {u_score}.\nToo much! You have lost...\n')
                self.result = False
                return False
            print(f'Your score: {u_score}.\nHit another? (y/n)')
        self.result = True
        return True

    def james_turn(self):
        self.james_set.set_of_cards = []
        self.james_hit()
        self.james_hit()
        print(self.james_set)
        j_score = self.james_set.score
        print(f'My score: {j_score}. ', end='')
        while j_score < self.user_set.score and j_score < 21:
            print('I\'ll take another...')
            self.james_hit()
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

    def the_bill(self):
        if self.result:
            self.player.win(self.pot)
        else:
            self.player.lost(self.pot)
        print(self.player)
