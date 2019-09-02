from core import ImageIdentifierStrategy


class MostLikedStrategy(ImageIdentifierStrategy):
    """Most Liked Strategy

    This class implements a strategy of
    identfying what image was liked the most

    Extends:
        ImageIdentifierStrategy
    """

    def __init__(self):
        pass

    def __new__(self, image_entities):
        return_entity = None
        for entity in image_entities:
            if return_entity:
                if entity.likes > return_entity.likes:
                    return_entity = entity
                continue
            else:
                return_entity = entity
        return return_entity
