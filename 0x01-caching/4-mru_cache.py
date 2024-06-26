#!/usr/bin/env python3
"""
    Module with MRUCache class implemeenting MRU cache replacement
    policy

"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRUCache is a caching sytem that inherits from BaseCaching"""

    def __init__(self):
        """Initializes an order list to keep track of keys"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Adds an item to the cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = self.order.pop()
                del self.cache_data[mru_key]
                print("DISCARD: {}".format(mru_key))

            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Gets an item from cache by key"""
        if key is None or key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
