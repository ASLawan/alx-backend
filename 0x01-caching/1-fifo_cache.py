#!/usr/bin/env python3
"""
    Module with class FIFOCache which is a caching system that
    inherits from BaseCaching

"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache is a caching system that inherits from BaseCaching"""

    def __init__(self):
        """Initializes an empty order list"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Adds an item to the cache"""
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    first_key = self.order.pop(0)
                    del self.cache_data[first_key]
                    print("DISCARD: {}".format(first_key))
                self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Gets an item from the cache by key"""
        if key is None:
            return None
        return self.cache_data.get(key)
