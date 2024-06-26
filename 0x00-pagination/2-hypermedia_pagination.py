#!/usr/bin/env python3
'''simple pagination'''
import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''get dataset from a page'''
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        index = index_range(page, page_size)
        dataset = self.dataset()
        if dataset is not None and index[0] > len(dataset):
            return []
        return dataset[index[0]:index[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10):
        '''get hyperlinks to dataset'''
        data = self.get_page(page, page_size)
        size = len(data)
        if page > 1:
            prev_page = page - 1
        else:
            prev_page = None
        total_pages = math.ceil(len(self.dataset()) / page_size)
        if page < total_pages:
            next_page = page + 1
        else:
            next_page = None
        hyper = {
                "page_size": size,
                "page": page,
                "data": data,
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": total_pages
                }
        return hyper
