#!/usr/bin/env python3
"""
This module contains a class FIFOCache
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    This class inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """ Initializing
        """
        super().__init__()

    def put(self, key, value):
        """ Add an item in the cache
        Args:
            key: the key
            value: the item to be stored in the cache
        """
        if key is None or value is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            del_key = list(self.cache_data.keys())[0]
            del self.cache_data[del_key]
            print("DISCARD: {}".format(del_key))
        self.cache_data[key] = value

    def get(self, key):
        """ Get an item by key from the cache
        Args:
            key: the key
        if key is None or item is None, return None
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
