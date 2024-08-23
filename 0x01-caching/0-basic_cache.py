#!/usr/bin/env python3
"""
This module contains a class BasicCache
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    This class inherits BaseCaching
    """

    def __init__(self):
        """ Initialize
        """
        # super().__init__(self)
        BaseCaching.__init__(self)

    def put(self, key, item):
        """ Add an item in the cache
        Args:
            key: key
            item: item
        if key or item is None, do nothing
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key from the cache
        Args:
            key: key
        if key is None or item is None, return None
        """
        if key is None:
            return None
        return self.cache_data.get(key)
