import pojos
import init

'''
File that contains the game instructions
'''

# start game
player = pojos.Player(name="Harold")

game = init
init.deal(player)
print(player.hand.cards[1].name)
