#!/usr/bin/env python3
'''
LFU caching
'''
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    '''A LFU cache class'''
    def __init__(self):
        '''initializes the class instance'''
        super().__init__()
        self.frequency = {}  # Tracks the frequency of access for each key
        self.order = {}  # Tracks the order of access for each key
        self.access_count = 0  # Global access counter to implement LRU within the same frequency

    def put(self, key, item):
        '''inserts an object in the cache data'''
        if key is None or item is None:
            return

        # If the key is already in the cache, update the item and frequency
        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.order[key] = self.access_count
            self.access_count += 1
            return

        # If the cache is full, we need to evict an item
        if len(self.cache_data) >= self.MAX_ITEMS:
            # Find the least frequently used keys
            min_freq = min(self.frequency.values())
            lfu_keys = [k for k, v in self.frequency.items() if v == min_freq]
            
            # If there's more than one LFU key, apply LRU to choose the eviction candidate
            if len(lfu_keys) > 1:
                lru_key = min(lfu_keys, key=lambda k: self.order[k])
            else:
                lru_key = lfu_keys[0]
                
            # Evict the selected key
            del self.cache_data[lru_key]
            del self.frequency[lru_key]
            del self.order[lru_key]
            print(f"DISCARD: {lru_key}")

        # Insert the new key-item pair
        self.cache_data[key] = item
        self.frequency[key] = 1
        self.order[key] = self.access_count
        self.access_count += 1

    def get(self, key):
        '''gets an item from cached data'''
        if key is None or key not in self.cache_data:
            return None
        # Update the frequency and order
        self.frequency[key] += 1
        self.order[key] = self.access_count
        self.access_count += 1
        return self.cache_data[key]
