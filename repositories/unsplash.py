"""
Repository functions for working with
unsplash data
"""
from entities import UnsplashImageEntityMapper
from resources import UnsplashImageResource


def fetch_unsplash_images(page_number=1):
    """Fetch Unsplash Images

    Perfroms a call to unsplash for images
    and returns entities for the same

    Keyword Arguments:
        page_number {number} -- [The page to request] (default: {1})

    Returns:
        [UnsplashImageEntity] -- [ UnsplashImageEntity Object]
    """
    return_list = []
    images = UnsplashImageResource().fetch_images(page_number)

    for image in images:
        return_list.\
            append(UnsplashImageEntityMapper().from_images_source(image))

    return return_list
