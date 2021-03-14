from game import Game

if __name__ == '__main__':

    game = Game()
    game.start()
    while game.decision():

        game.bet()
        if game.user_turn():
            game.james_turn()
            game.check()
        game.the_bill()
        if game.player.cash <= 0:
            print('You are out of money.\nG A M E    O V E R')
            break
        print('Another round? (y/n)')

    if game.player.cash > 0:
        print(f'You\'ve won {game.player.cash}$ See you next time!')
