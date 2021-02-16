"""
Authentication class specific to Unsplash image source API requirements
"""
from config import settings
from core import AuthenticationResource


class UnsplashAuthenticationResource(AuthenticationResource):
    """
    Unsplash Authentication resource

    Holds basic methods for interacting with the Unsplash API
    """

    base_url = settings.UNSPLASH_BASE_URL
    home_url = settings.UNSPLASH_HOME_URL
    search_url = settings.UNSPLASH_SEARCH_URL
    client_id = settings.CLIENT_ID
    limit = settings.RESULTS_PER_PAGE

    def __init__(self):
        super().__init__()

    @property
    def get_base_url(self) -> str:
        """Build base url string"""
        return "{}?client_id={}&per_page={}".format(
            self.base_url, self.client_id, self.limit
        )

    def get_photos_url(self, page_number=1):
        """Build base for fetching photots"""
        return "{}{}?client_id={}&per_page={}&page={}".format(
            self.base_url, self.home_url, self.client_id, self.limit, page_number
        )

    def get_photos_by_search(self, search_query, page_number=1) -> str:
        """Search base URL"""
        return "{}{}?client_id={}&per_page={}&query={}&page={}".format(
            self.base_url,
            self.search_url,
            self.client_id,
            self.limit,
            search_query,
            page_number,
        )
