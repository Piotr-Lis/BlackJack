class Card:

    def __init__(self, figure, colour):
        self.figure = figure
        self.colour = colour

    def __eq__(self, other):
        return True if self.figure == other.figure and self.colour == other.colour else False

    @property
    def point(self):
        point_table = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                   '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10,
                   'K': 10, 'A': 11}
        return point_table[self.figure]

    def __repr__(self):
        colours = {'heart': '\u2764', 'diamond': '\u25c6',
                   'spade': '\u2663', 'club': '\u2660'}
        return self.figure + colours[self.colour]

