from cardset import CardSet

class User:

    cash = 1000

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}: {self.cash}$'

    def win(self, pot):
        self.cash += pot

    def lost(self, pot):
        self.cash -= pot


if __name__ == '__main__':

    player = User('Piotr')
    print(player)