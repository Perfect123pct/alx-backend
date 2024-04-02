#!/usr/bin/env python3
"""LFUCache module"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache inherits from BaseCaching and implements a caching system
    using the Least Frequently Used (LFU) algorithm.
    """

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.freq_counter = {}

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Increment the frequency counter for the key
            self.freq_counter[key] += 1
        else:
            # Add a new key with frequency 1
            self.freq_counter[key] = 1

        if len(self.cache_data) >= self.MAX_ITEMS:
            # Find the least frequently used item(s)
            min_freq = min(self.freq_counter.values())
            least_frequent_keys = [k for k, v in self.freq_counter.items() if v == min_freq]

            # If there are multiple least frequent items, use LRU to break tie
            if len(least_frequent_keys) > 1:
                lru_key = min(self.cache_data, key=lambda k: self.cache_data[k])
                del self.cache_data[lru_key]
                del self.freq_counter[lru_key]
                print("DISCARD:", lru_key)
            else:
                # Delete the least frequently used item
                del self.cache_data[least_frequent_keys[0]]
                del self.freq_counter[least_frequent_keys[0]]
                print("DISCARD:", least_frequent_keys[0])

        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        # Increment the frequency counter for the key
        self.freq_counter[key] += 1

        return self.cache_data[key]


if __name__ == "__main__":
    my_cache = LFUCache()
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
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
    my_cache.put("L", "L")
    my_cache.print_cache()
    my_cache.put("M", "M")
    my_cache.print_cache()

