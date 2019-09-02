from abc import ABC


class ImageEntityMapper(ABC):
    """

    """

    def to_images_model(self):
        pass

    def from_images_model(self):
        pass

    def to_images_source(self):
        pass

    def from_images_source(self, source_data: dict):
        pass
