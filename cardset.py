from card import Card
from random import randint


class CardSet:

    def __init__(self):
        self.set_of_cards = []

    def __repr__(self):
        return str(self.set_of_cards)

    def __contains__(self, key):
        return True if key in self.set_of_cards else False

    def __len__(self):
        return len(self.set_of_cards)

    @property
    def score(self):
        score = sum([card.point for card in self.set_of_cards])
        aces = [Card('A', 'heart'), Card('A', 'diamond'), Card('A', 'spade'), Card('A', 'club')]
        for card in aces:
            if score > 21 and card in self:
                score -= 10
        return score

    def new_deck(self):
        figures = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
        colours = 'heart diamond spade club'.split()
        for fig in figures:
            for col in colours:
                self.set_of_cards.append(Card(fig, col))

    def take_card(self, source):
        self.set_of_cards.append(source.set_of_cards.pop(randint(0, len(source)-1)))