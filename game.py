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

    printGameStatusCompHidden(player1, comp1)


def printGameStatus(player1, comp1):
    print("\n**************")
    print("GAME STATUS")
    print("**************")
    print("- PLAYER HAND -")
    for ph in player1.hand:
        print(ph.name)

    print("\n- COMPUTER HAND -")
    for ph in comp1.hand:
        print(ph.name)

    print("\n- BET (Bankroll) -")
    print(f'{player1.bet} ({player1.bankroll}) ')


def printGameStatusCompHidden(player1, comp1):
    print("\n**************")
    print("GAME STATUS")
    print("**************")
    print("- PLAYER HAND -")
    for ph in player1.hand:
        print(ph.name)

    print("\n- COMPUTER HAND -")
    print(f'{comp1.hand[0].name} - XX')

    print("\n- Bet (Bankroll) -")
    print(f'{player1.bet} ({player1.bankroll}) ')


def playAgain(p1):
    while True:
        playagain = input(f"You got {p1.bankroll} in bank. Wanna play again (y/n) ? ")
        if playagain == 'y':
            print(chr(27) + "[2J")
            g = Game()
            p1.hand = []
            g.start(p1)
            break
        elif playagain == 'n':
            break
        else:
            print("Try again")


def computerTurn(p1, c1, deck, gameON):
    print("--------------- COMPUTER TURN --------------------")
    totalP1 = pojos.calculateTotal(p1.hand)
    totalC1 = pojos.calculateTotal(c1.hand)
    while totalC1 <= totalP1 and totalC1 < 21 and gameON:
        printGameStatus(p1, c1)
        # computer hit
        if c1.hit(deck) == -1:
            gameON = False
            printGameStatus(p1, c1)
            p1.bankroll = p1.bankroll + 2*p1.bet
            p1.bet = 0
            print(f'---------   Computer Bust. THE WINNER IS {p1.name}. CONGRATS! ----------------')
            playAgain(p1)
            break
        else:
            totalC1 = pojos.calculateTotal(c1.hand)
    else:
        printGameStatus(p1, c1)
        p1.bet = 0
        print(f'---------   Computer wins, GG, go learn how to play! ----------------')
        playAgain(p1)


class Game:

    def __init__(self):
        pass

    def start(self,p1):
        # start game
        if p1.bankroll == 0:
            print("Go work, make money, and then come and play!")
        else:
            self.gameON = True
            deck = pojos.Deck()
            # Player bet
            while p1.placeBet(input(f"\nHow much do you bet: (upto {p1.bankroll}) ")) in [-1,-2]:
                print("Try again")

            # Deal
            c1 = pojos.Computer([])
            deal(deck, p1, c1)

            # Choice of hit or check
            while True:
                choice = input("Would you like to hit? (y/n) ")

                if choice not in ['y','n']:  # try again
                    print("Try again")

                if choice == 'n':  # check
                    total = p1.check()
                    if total == 21:
                        p1.bankroll = p1.bankroll + 2*p1.bet
                        p1.bet = 0
                        print(f'---------   Computer Bust. THE WINNER IS {p1.name}. CONGRATS! ----------------')
                        playAgain(p1)
                    else:
                        print(f"Total value is {total}")
                    break

                if choice == 'y':
                    if p1.hit(deck) == -1:
                        self.gameON = False
                        printGameStatusCompHidden(p1, c1)
                        print("BUST!!!! GAME OVER!!! YOU LOSE, HAHAHA!")
                        playAgain(p1)
                        break
                    else:
                        printGameStatusCompHidden(p1, c1)

            # Computer turn
            if self.gameON:
                computerTurn(p1, c1, deck, self.gameON)


print(chr(27) + "[2J")
print("\n##########################")
print("#  LETS PLAY BLACKJACK     #")
print("##########################")
g = Game()
g.start(pojos.Player("Harold",[],0))
