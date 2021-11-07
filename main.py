import random
import itertools


# establishing cards
class Deck:
    suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
    values = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

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


