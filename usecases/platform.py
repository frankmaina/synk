from repositories import fetch_unsplash_images
from strategies import MostLikedStrategy
import urllib.request
from config import settings
import ctypes
import os


def provides_identification_strategy():
    """Return Identifcatoin strategy"""
    return MostLikedStrategy


class Platfrom:
    """Platfrom

    Interfacing class that works with the OS
    """

    def __init__(self):
        self.identification_strategy = provides_identification_strategy()

    def identify_image(self):
        """Returns a the selected image"""
        entities = fetch_unsplash_images()
        image = self.identification_strategy(entities)
        return image

    def download_image(self, image_entity):
        """Saves the image locally"""
        local_path = "{}/{}".format(
            settings.LOCAL_STORAGE_PATH, "{}.jpg".format(image_entity.source_id)
        )
        urllib.request.urlretrieve(image_entity.image_url, local_path)
        image_entity.local_path = local_path
        return image_entity

    def set_image(self, image_entity):
        """
        Perform os types update calls
        :param image_entity:
        """
        # TODO: Set conditional checks for platfrom specific calls
        spi_setdeskwallpaper = 20
        ctypes.windll.user32.SystemParametersInfoW(
            spi_setdeskwallpaper, 0, os.path.abspath(image_entity.local_path), 3
        )

    def defaut_set(self):
        """Runs default platfrom functions"""
        self.set_image(self.download_image(self.identify_image()))
