#!/usr/bin/env python3
"""
This module contains a class LIFOCache
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ This Class inherits from BaseCaching and implements LAST IN FIRST OUT
    """

    def __init__(self):
        """ Initializing
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache.

        Args:
            key (str): The key of the item to be added.
            item (any): The item to be added.

        Returns:
            None
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key, _ = self.cache_data.popitem()
            print("DISCARD: {}".format(last_key))
        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key from the cache.
        Args:
            key (str): The key of the item to be retrieved.
        Returns:
            any: The item associated with the key if it exists in the cache, otherwise None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
        