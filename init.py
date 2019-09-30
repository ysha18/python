import pojos
import random


# Creation of suit
def createSuit(suitName):
    as1Card = pojos.Card("A " + suitName, 1)
    valetCard = pojos.Card("V " + suitName, 10)
    queenCard = pojos.Card("Q " + suitName, 10)
    kingCard = pojos.Card("K " + suitName, 10)

    suit = [as1Card, valetCard, queenCard, kingCard]

    for i in range(2, 10):
        c = pojos.Card(name=str(i) + " " + suitName, value=i)
        suit.append(c)

    # for c in suit:
    # 	print(f"{c.name} - {c.value}")

    return suit


# END Creation of suit. #####


# Creation of deck
class Deck:
    card = pojos.Card

    def __init__(self):
        diamonds = createSuit("Diamonds")
        clubs = createSuit("Club")
        hearts = createSuit("Heart")
        spades = createSuit("Spade")
        self.cards = [diamonds, clubs, hearts, spades]
        print("Deck created")

    def getRansomCard(self):
        n1 = random.randint(0, 3)
        n2 = random.randint(0, 11)
        return self.cards[n1][n2]


# deck = Deck()
# print(f"Deck length:  {len(deck.cards)}")
# print(f"Suit length:  {len(deck.cards[0])}")
# n1 = random.randint(0, 3)
# n2 = random.randint(0, 11)
# print(f'{n1} - {n2}')
# print(deck.cards[n1][n2].name)

class Game:
    def deal(self,player,computer):
        deck = Deck()
        c1 = deck.getRansomCard()
        c2 = deck.getRansomCard()
        handPlayer = pojos.Hand([c1, c2])
        player.hand = handPlayer
        c3 = deck.getRansomCard()
        c4 = deck.getRansomCard()

        print(c1.name)
