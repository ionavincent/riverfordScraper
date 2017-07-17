import requests
import requests_cache


class Scraper(object):

    def __init__(self, cache_name, cache_expiry):
        requests_cache.install_cache(
            cache_name,
            backend='sqlite',
            expire_after=cache_expiry,
            allowable_methods=("GET",)
        )

    def get(self, url, headers=None):
        """Get HTML from an URL and parse it"""
        if not headers:
            headers = {}
        response = requests.get(url, headers=headers)
        return response.text
