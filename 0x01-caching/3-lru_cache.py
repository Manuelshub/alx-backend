#!/usr/bin/env python3
"""
This module contains a class LRUCache
"""
from base_caching import BaseCaching
from typing import OrderedDict


class LRUCache(BaseCaching):
    """
    This class inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """ Initializing
        """
        super().__init__()
        self.lru_cache = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        Args:
            key: the key
            item: the item to be stored in the cache
        """
        if key is None or item is None:
            return

        self.lru_cache[key] = item
        self.lru_cache.move_to_end(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.lru_cache))
            del self.cache_data[first_key]
            print("DISCARD: {}".format(first_key))

        if len(self.lru_cache) > BaseCaching.MAX_ITEMS:
            self.lru_cache.popitem(last=False)

    def get(self, key):
        """
        Retrieves a value from the cache by its key.

        Args:
            key (str): The key of the value to be retrieved.

        Returns:
            any: The value associated with the key if it
            exists in the cache, otherwise None.
        """
        if key is None or key not in self.cache_data:
            return None
        self.lru_cache.move_to_end(key)
        return self.cache_data[key]
