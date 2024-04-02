#!/usr/bin/env python3
"""FIFOCache module"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache inherits from BaseCaching and implements a caching system
    using the First-In-First-Out (FIFO) algorithm.
    """

    def __init__(self):
        """Initialize"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            # Discard the first item put in cache (FIFO algorithm)
            first_item = next(iter(self.cache_data))
            print("DISCARD:", first_item)
            del self.cache_data[first_item]

        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]


if __name__ == "__main__":
    my_cache = FIFOCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    my_cache.put("F", "Mission")
    my_cache.print_cache()

