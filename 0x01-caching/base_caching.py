#!/usr/bin/env python3
"""
    BaseCaching Module

"""


class BaseCaching():
    """BaseCaching defines:
        - constants of your caching system
        - where your data are stored
    """
    MAX_ITEMS = 4

    def __init__(self):
        """Initializes an empty dictionary"""
        self.cache_data = {}

    def print_cache(self):
        """Prints the cache"""
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """Adds an item to the cache"""
        raise NotImplementedError("put must be implemented\
                                  in your cache class")

    def get(self, key):
        """Gets an item by key"""
        raise NotImplementedError("get must be implemented\
                                  in your cache class")
