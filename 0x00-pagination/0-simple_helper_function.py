#!/usr/bin/env python3
'''pagination func'''


def index_range(page: int, page_size: int) -> tuple:
    '''returns the index of a page'''
    end = page * page_size
    start = end - page_size
    return (start, end)
