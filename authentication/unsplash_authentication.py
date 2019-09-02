"""

"""
from core import AuthenticationResource
from config import environment
from config import settings


class UnsplashAuthenticationResource(AuthenticationResource):

    base_url = "https://api.unsplash.com/"
    home_url = "photos/"
    search_url = "search/photos/"
    client_id = "9955adb335125f198456bd5cd4103f2a128cef37294bd57839b64b89102f3bc3"
    limit = "20"

    def __init__(self):
        super().__init__()

    @property
    def get_base_url(self) -> str:
        return "{}?client_id={}&per_page={}".format(
            self.base_url, self.client_id, self.limit)

    def get_photos_url(self, page_number=1):
        return "{}{}?client_id={}&per_page={}&page={}".format(
            self.base_url, self.home_url, self.client_id, self.limit,
            page_number)

    def get_photos_by_search(self, search_query, page_number=1) -> str:
        return "{}{}?client_id={}&per_page={}&query={}&page={}".format(
            self.base_url, self.search_url, self.client_id, self.limit,
            search_query, page_number)
