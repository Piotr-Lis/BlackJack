from game import Game

if __name__ == '__main__':

    game = Game()
    print('#### BLACK JACK ####')
    print('Hi! My name is James. Wanna play? (y/n)')
    while game.decision():
        if game.user_turn():
            game.james_turn()
            game.check()
        print('Another round? (y/n)')
    print('See you!')
