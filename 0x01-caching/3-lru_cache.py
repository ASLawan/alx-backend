#!/usr/bin/env python3
"""
    Module implementing LRUCache caching system that inherits from
    BaseCaching class

"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Caching system that inherits from BaseCache class"""

    def __init__(self):
        """Initializes an empty order list for keys"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Adds an item to the cache dictionary"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.order.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD: {}".format(lru_key))

            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Gets an item from cache by key"""
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
