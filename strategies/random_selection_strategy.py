from core import ImageIdentifierStrategy
import random


class RandomSelectionStrategy(ImageIdentifierStrategy):
    """Random Selection Strategy

    Chooses a "random" entity from the image
    image selection

    Extends:
        ImageIdentifierStrategy
    """

    def __init__(self):
        pass

    def __new__(self, image_entities):
        return random.choice(image_entities)
