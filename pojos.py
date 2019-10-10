import random

"""
Script to define the pojos
"""


# Definition card
class Card:
    def __init__(self, name, value):
        self.name = name
        self.value = value


# Creation of deck
class Deck:
    cards = []

    def __init__(self):
        diamonds = createSuit("Diamonds")
        clubs = createSuit("Club")
        hearts = createSuit("Heart")
        spades = createSuit("Spade")

        self.cards.extend(diamonds + clubs + hearts + spades)

        # for card in self.cards:
        #     print(f'{card.name}')
        print("Deck created")

    def shuffle(self):
        return random.shuffle(self.cards)


# Creation of suit
def createSuit(suitName):
    as1Card = Card("A " + suitName, 1)
    valetCard = Card("V " + suitName, 10)
    queenCard = Card("Q " + suitName, 10)
    kingCard = Card("K " + suitName, 10)

    suit = [as1Card, valetCard, queenCard, kingCard]

    for i in range(2, 10):
        c = Card(name=str(i) + " " + suitName, value=i)
        suit.append(c)

    # for c in suit:
    # 	print(f"{c.name} - {c.value}")

    return suit


# END Creation of suit. #####


class Hand:

    def __int__(self, cards):
        self.cards = cards


# Definition player
def calculateTotal(hand):
    total = 0
    for card in hand:
        total += card.value
    return total


class Player:

    def __init__(self, name, hand, bet):
        self.name = name
        self.hand = hand
        self.bankroll = 1000
        self.bet = bet

    def placeBet(self, amount):
        try:
            if int(amount) > self.bankroll:
                print("Not enough money to bet")
                return -1
            print("passed 1st step")
            self.bet = int(amount)
            self.bankroll = self.bankroll - int(amount)
            print(f'Amount left in bankroll: {self.bankroll}')
        except (ValueError,TypeError):
            print(f"Can't bet, there is an error")
            return -2

    def hit(self, deck):
        print("\n---> Player hit")
        self.hand.append(deck.cards.pop())
        totalPlayer = calculateTotal(self.hand)
        if totalPlayer > 21:
            return -1

    def check(self):
        total = calculateTotal(self.hand)
        return "Total value is " + str(total)


# testing Player class 
# p1 = Player(name="Harold")
# print(p1.name)


# p1.bet(abc)


class Computer:

    def __init__(self, hand):
        self.hand = hand

    def hit(self, deck):
        print("\n---> Computer hit")
        self.hand.append(deck.cards.pop())
        totalPlayer = calculateTotal(self.hand)
        if totalPlayer > 21:
            return -1
