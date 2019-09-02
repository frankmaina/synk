"""
CLass for resource
"""
from abc import ABC


class Resource(ABC):
    """

    """

    def __init__(self):
        self.resource_name = None
        pass

    def fetch_images(self):
        pass

    def get_image_by_id(self):
        pass

    def get_resource_name(self):
        return self.resource_name
