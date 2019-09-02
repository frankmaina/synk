from authentication import UnsplashAuthenticationResource


def provides_unsplash_authentication_resource():
    """Returns the authentication class to use"""
    return UnsplashAuthenticationResource
