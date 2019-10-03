import pojos

"""
File that contains the game instructions
"""


def deal(deck, player1, comp1):
    deck.shuffle()
    # Get player & comp hand
    for i in range(2):
        player1.hand.append(deck.cards.pop())
    comp1.hand.append(deck.cards.pop())
    # print(f'ZZZZZZZ {player1.hand[0].name} {comp1.hand[0].name})')

    printGameStatus(player1, comp1)


def printGameStatus(player1, comp1):
    print("\n-- GAME STATUS --\n")
    print("- PLAYER HAND -")
    for ph in player1.hand:
        print(ph.name)

    print("\n- COMPUTER HAND -")
    print(f'{comp1.hand[0].name} - XX')

    print("\n- BET -")
    print(f'{player1.bet} ')

    print("\n- BANKROLL -")
    print(f'{player1.bankroll} ')
    print("\n------------\n")


# start game
print("\n**************************")
print("*  LETS PLAY BLACKJACK     *")
print("****************************\n")

deck = pojos.Deck()
p1 = pojos.Player('Harold', [], 0)
c1 = pojos.Computer([])
deal(deck, p1, c1)

# Player bet
playerbet = input("How much do you bet: ")
p1.placeBet(int(playerbet))
printGameStatus(p1, c1)

# Choice of hit or check
choice = 'y'
while choice == 'y' or not pojos.gameON:
    choice = input("Would you like to hit: ")
    if choice == 'y':
        print(p1.hit(deck))
        printGameStatus(p1, c1)
    else:
        print(p1.check())
printGameStatus(p1, c1)
