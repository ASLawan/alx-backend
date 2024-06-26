#!/usr/bin/env python3
"""
    Module implementing a LFUCache class, a caching system
    that inherits from BaseCaching

"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache is a caching system that inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.usage_count = {}
        self.order = []

    def put(self, key, item):
        """ Adds an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_count[key] += 1
            self.order.remove(key)
            self.order.append(key)
        else:
            # If the cache is full, evict the least frequently used item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu_key = min(self.usage_count, key=lambda k:
                              (self.usage_count[k], self.order.index(k)))
                del self.cache_data[lfu_key]
                del self.usage_count[lfu_key]
                self.order.remove(lfu_key)
                print("DISCARD: {}".format(lfu_key))

            # Add the new key to the cache
            self.cache_data[key] = item
            self.usage_count[key] = 1
            self.order.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        self.usage_count[key] += 1
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
