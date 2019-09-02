from core import ImageEntityMapper
from core.entities import ImageEntity
from resources import UnsplashImageResource


class UnsplashImageEntityMapper(ImageEntityMapper):
    """Unsplash Image Entity Mapper

    Maps values from unsplash data to a standard entity

    Extends:
      ImageEntityMapper
    """

    def __init__(self):
        pass

    def to_images_model(self):
        pass

    def from_images_model(self):
        pass

    def to_images_source(self):
        pass

    def from_images_source(self, source_data: dict):
        super(UnsplashImageEntityMapper, self).to_images_source()
        return ImageEntity(source_id=source_data['id'],
                           image_url=source_data['urls']['raw'],
                           image_height=source_data['height'],
                           image_width=source_data['width'],
                           description=source_data['alt_description'],
                           source=UnsplashImageResource,
                           likes=source_data['likes'])
