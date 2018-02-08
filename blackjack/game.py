from itertools import product
import random

from .card import Card, RANKS, SUITS


class Blackjack(object):

    def __init__(self, decks=6):
        self.decks = decks

        self.initialise_cards()

    def validate_decks(self):
        if self.decks < 1:
            raise ValueError(f'Too few decks: {self.decks}')

    def initialise_cards(self):
        self.validate_decks()

        self.cards = [
            Card(rank=rank['type'], suit=suit['type'])
            for rank, suit
            in self.decks * list(product(RANKS.values(), SUITS.values()))
        ]

        self.shuffle_cards()

        self.initialise_blank_card_height()

    def shuffle_cards(self):
        random.shuffle(self.cards)

    def initialise_blank_card_height(self):
        self.blank_card_height = random.randint(1, len(self.cards) // 6)
