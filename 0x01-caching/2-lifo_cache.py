#!/usr/bin/env python
"""
    Module with caching sytem class LIFOCache that inherits
    from BaseCaching class

"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class that inherits from BaseCaching class"""

    def __init__(self):
        """Initializes list to keep track of cache items"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Adds an item to the cache dictionary"""
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    last_key = self.order.pop()
                    del self.cache_data[last_key]
                    print("DISCARD: {}".format(last_key))
                self.order.append(key)
            self.cache_data[key] = item
        elif key in self.cache_data and item:
            self.order.remove(key)
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Gets an item from the cache dictionary by key"""
        if key is None:
            return None
        return self.cache_data.get(key)
