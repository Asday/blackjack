import unittest

from blackjack.card import Card, RANKS, SUITS


class CardTest(unittest.TestCase):

    def test_validate_raises_for_invalid_cards(self):
        invalid_suit = Card(rank=RANKS[2]['type'], suit='INVALID')
        invalid_rank = Card(rank='INVALID', suit=SUITS['hearts']['type'])
        invalid_suit_and_rank = Card(rank='INVALID', suit='INVALID')

        self.assertRaises(Exception, invalid_suit.validate)
        self.assertRaises(Exception, invalid_rank.validate)
        self.assertRaises(Exception, invalid_suit_and_rank.validate)
