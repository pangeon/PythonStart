"""
Class representing one card:
    value, color and file with image
"""


class Card:
    VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'As']

    COLORS = ['♥', '♦', '♣', '♠']

    def __init__(self, value, color):
        """Init card - value and color."""
        self._value = value
        self._color = color

    @property
    def value(self):
        """Return card value"""
        return self._value

    @property
    def color(self):
        """Return card color"""
        return self._color

    @property
    def file_name(self):
        """Return image file name"""
        images = []
        colors = ['_heart', '_diamond', '_club', '_spade']
        for card_index in range(len(self.VALUES)):
            for color_index in range(4):
                images.append(str.lower(self.VALUES[card_index]) + colors[color_index] + ".png")

        return images

    def __repr__(self):
        """Return official text representing of card"""
        return f"Card(value='{self.value}, color='{self.color}')"

    def __str__(self):
        """Return official text representing of card"""
        return f'{self.value} {self.color}'

    def __format__(self, format):
        """Return formatting text representing of card"""
        return f'{str(self):{format}}'


