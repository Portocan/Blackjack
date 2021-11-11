import itertools
import random

class Deck:
    suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
    values = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King",
              "Ace"]

    def __init__(self):
        self.cards = []

# actual deck creation using Card class
    @property
    def createdeck(self):
        for suit, value in itertools.product(self.suits, self.values):
            self.cards.append(Card(suit, value))
        return self.cards

    def shuffledeck(self):
        random.shuffle(self.cards)
        return self.cards

    def cleardeck(self):
        self.cards = []
        return self.cards


class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # card print statement
    def __str__(self):
        return self.value + " of " + self.suit

    # assigning value to each card
    def cardvalue(self):
        if self.value in ["Jack", "Queen", "King"]:
            return 10
        if self.value in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            return int(self.value)
        if self.value == "Ace":
            return 1

class Player:

    def __init__(self, hand):
        self.hand = []

    def reset(self):
        self.hand = []

    def loadhand(self):
        print("Players Hand:")

class Game:
        def __init__(self):
            self.deck = []

        def play(self):
            self.deck = Deck()
            self.deck.createdeck()



#testing area
game = Game()
game.play()

