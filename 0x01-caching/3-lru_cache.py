#!/usr/bin/env python3
"""LRUCache module"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache inherits from BaseCaching and implements a caching system
    using the Least Recently Used (LRU) algorithm.
    """

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.used_order = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        # Update used_order when accessing an existing key
        if key in self.cache_data:
            self.used_order.remove(key)
        else:
            # Remove least recently used item if cache is full
            if len(self.cache_data) >= self.MAX_ITEMS:
                lru_key = self.used_order.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD:", lru_key)

        self.cache_data[key] = item
        self.used_order.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        # Update used_order when accessing an existing key
        self.used_order.remove(key)
        self.used_order.append(key)

        return self.cache_data[key]


if __name__ == "__main__":
    my_cache = LRUCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    print(my_cache.get("B"))
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
    my_cache.put("H", "H")
    my_cache.print_cache()
    my_cache.put("I", "I")
    my_cache.print_cache()
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()

