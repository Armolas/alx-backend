#!/usr/bin/env python3
'''
lifo caching
'''
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''A LIFO cache class'''
    def __init__(self):
        '''initializes the class instance'''
        super().__init__()
        self.order = []

    def put(self, key, item):
        '''inserts an object in the cache data'''
        if key is None or item is None:
            return
        if key in self.order:
            self.order.remove(key)
        if len(
                self.cache_data
                ) >= self.MAX_ITEMS and key not in self.cache_data:
            to_del = self.order.pop()
            del (self.cache_data[to_del])
            print(f"DISCARD: {to_del}")
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        '''gets an item from cached data'''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
