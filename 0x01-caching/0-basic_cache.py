#!/usr/bin/env python3
'''
Basic cache Module
'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''This is a Basic Cache class'''
    def put(self, key, item):
        '''stores a cache data'''
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        '''gets a cache item'''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
