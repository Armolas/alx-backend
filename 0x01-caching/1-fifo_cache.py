#!/usr/bin/env python3
'''
fifo caching
'''
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''A FIFO cache class'''
    def __init__(self):
        '''initializes the class instance'''
        super().__init__()

    def put(self, key, item):
        '''inserts an object in the cache data'''
        if key is None or item is None:
            return
        if len(
                self.cache_data
                ) >= self.MAX_ITEMS and key not in self.cache_data:
            to_del = next(iter(self.cache_data))
            del (self.cache_data[to_del])
            print(f"DISCARD: {to_del}")
        self.cache_data[key] = item

    def get(self, key):
        '''gets an item from cached data'''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
