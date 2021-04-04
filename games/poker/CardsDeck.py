"""Class representing cards deck"""

import random
from Card import Card


class CardsDeck:
    NUMBER_OF_CARDS = 52

    def __init__(self):
        """Init cards deck"""
        self._current_card = 0
        self._cards_deck = []

        for i in range(CardsDeck.NUMBER_OF_CARDS):
            self._cards_deck.append(Card(Card.VALUES[i % 13], Card.COLORS[i // 13]))

    def randomize_card_position(self):
        """Shuffling the card deck"""
        self._current_card = 0
        random.shuffle(self._cards_deck)

    def next_card(self):
        """Return single card from deck"""
        try:
            card = self._cards_deck[self._current_card]
            self._current_card += 1
            return card
        except:
            return None

    def __str__(self):
        """Return cards deck representation"""
        string_deck_representation = ''
        for index, card in enumerate(self._cards_deck):
            string_deck_representation += f'{self.next_card():<19}'
            if (index + 1) % 4 == 0:
                string_deck_representation += '\n'

        return string_deck_representation


