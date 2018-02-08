import attr


COLOUR_RED = 'colour_red'
COLOUR_BLACK = 'colour_black'


SUIT_CLUBS = 'suit_clubs'
SUIT_DIAMONDS = 'suit_diamonds'
SUIT_HEARTS = 'suit_hearts'
SUIT_SPADES = 'suit_spades'


SUITS = {
    'clubs': {
        'type': SUIT_CLUBS,
        'name': 'Clubs',
        'colour': COLOUR_BLACK,
    },
    'diamonds': {
        'type': SUIT_DIAMONDS,
        'name': 'Diamonds',
        'colour': COLOUR_RED,
    },
    'hearts': {
        'type': SUIT_HEARTS,
        'name': 'Hearts',
        'colour': COLOUR_RED,
    },
    'spades': {
        'type': SUIT_SPADES,
        'name': 'Spades',
        'colour': COLOUR_BLACK,
    },
}


RANK_ACE = 'rank_ace'
RANK_2 = 'rank_2'
RANK_3 = 'rank_3'
RANK_4 = 'rank_4'
RANK_5 = 'rank_5'
RANK_6 = 'rank_6'
RANK_7 = 'rank_7'
RANK_8 = 'rank_8'
RANK_9 = 'rank_9'
RANK_10 = 'rank_10'
RANK_JACK = 'rank_jack'
RANK_QUEEN = 'rank_queen'
RANK_KING = 'rank_king'


RANKS = {
    'ace': {
        'type': RANK_ACE,
        'name': 'Ace',
        'value_low': 1,
        'value_high': 11,
    },
    2: {
        'type': RANK_2,
        'name': 'Two',
        'value_low': 2,
        'value_high': 2,
    },
    3: {
        'type': RANK_3,
        'name': 'Three',
        'value_low': 3,
        'value_high': 3,
    },
    4: {
        'type': RANK_4,
        'name': 'Four',
        'value_low': 4,
        'value_high': 4,
    },
    5: {
        'type': RANK_5,
        'name': 'Five',
        'value_low': 5,
        'value_high': 5,
    },
    6: {
        'type': RANK_6,
        'name': 'Six',
        'value_low': 6,
        'value_high': 6,
    },
    7: {
        'type': RANK_7,
        'name': 'Seven',
        'value_low': 7,
        'value_high': 7,
    },
    8: {
        'type': RANK_8,
        'name': 'Eight',
        'value_low': 8,
        'value_high': 8,
    },
    9: {
        'type': RANK_9,
        'name': 'Nine',
        'value_low': 9,
        'value_high': 9,
    },
    10: {
        'type': RANK_10,
        'name': 'Ten',
        'value_low': 10,
        'value_high': 10,
    },
    'jack': {
        'type': RANK_JACK,
        'name': 'Jack',
        'value_low': 10,
        'value_high': 10,
    },
    'queen': {
        'type': RANK_QUEEN,
        'name': 'Queen',
        'value_low': 10,
        'value_high': 10,
    },
    'king': {
        'type': RANK_KING,
        'name': 'King',
        'value_low': 10,
        'value_high': 10,
    },
}


@attr.s
class Card(object):
    rank = attr.ib()
    suit = attr.ib()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.validate()

    def validate(self):
        errors = []
        if self.rank not in RANKS:
            errors.append(f'Invalid rank:  {self.rank}')

        if self.suit not in SUITS:
            errors.append(f'Invalid suit:  {self.suit}')

        if errors:
            raise ValueError(','.join(errors))
