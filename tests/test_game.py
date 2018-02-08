import unittest

from blackjack.game import Blackjack


class BlackjackTest(unittest.TestCase):

    def test_initialise_blank_card_height(self):
        blackjack = Blackjack()

        blackjack.initialise_blank_card_height()

        self.assertIsInstance(blackjack.blank_card_height, int)

    def test_initialise_cards_creates_the_right_amount_of_cards(self):
        blackjack = Blackjack()

        blackjack.decks = 1
        blackjack.initialise_cards()

        self.assertEqual(len(blackjack.cards), 52)

    def test_deck_amount_must_be_positive(self):
        blackjack = Blackjack()

        blackjack.decks = 0

        self.assertRaises(Exception, blackjack.validate_decks)
