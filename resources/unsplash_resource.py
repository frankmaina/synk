"""

"""
from core import Resource
from resources.factory import provides_unsplash_authentication_resource
from repositories import retrieve_data


class UnsplashImageResource(Resource):
    """Unsplash image Resource

    Data resource for unsplash.com
    """

    authentication_resource = provides_unsplash_authentication_resource()

    def __init__(self):
        super().__init__()
        self.resource_name = "Unsplash API"

    def fetch_images(self, page_number=1):
        return retrieve_data(
            self.authentication_resource().get_photos_url(page_number=page_number)
        )

    def search_images(self, query_term: str):
        return retrieve_data(
            self.authentication_resource().get_photos_by_search(query_term)
        ).json()
