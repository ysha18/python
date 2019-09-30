'''
Script to define the pojos
'''


# Definition card
class Card:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Hand:
    cards = []

    def __init__(self):
        pass


# Definition player
class Player:

    hand = Hand()

    def __init__(self, name):
        self.name = name
        self.bankroll = 1000

    def bet(self, amount):
        try:
            self.bankroll = self.bankroll - amount
            print(f'Amount left in bankroll: {self.bankroll}')
        except:
            print(f"Can't bet, there is an error")


# testing Player class 
# p1 = Player(name="Harold")
# print(p1.name)


# p1.bet(abc)


class Computer:
    def __init__(self, hand):
        self.hand = hand
