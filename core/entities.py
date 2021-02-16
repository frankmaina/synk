"""
Image Entity
"""


class ImageEntity:
    """Image Entity

    Concrete class reponsible for creating an abtraction
    between data sources and implementation

    Extends:
        ImageEntity
    """

    def __init__(
        self,
        source_id=None,
        image_url=None,
        image_height=None,
        image_width=None,
        description=None,
        likes=None,
        dislikes=None,
        source=None,
        local_path=None,
    ):

        self.source_id = source_id
        self.image_url = image_url
        self.image_height = image_height
        self.image_width = image_width
        self.description = description
        self.likes = likes
        self.dislikes = dislikes
        self.source = source
        self.local_path = local_path

    def __str__(self):
        return "Image Entity({})".format(self.source_id)
