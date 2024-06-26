#!/usr/bin/env python3
"""
    Module implementing BasicCache class the inherits BaseCaching
    class

"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """class inheriting BaseCaching class"""

    def put(self, key, item):
        """Adds an item to the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Gets and item from cache by key"""
        if key is None:
            return None
        return self.cache_data.get(key)
