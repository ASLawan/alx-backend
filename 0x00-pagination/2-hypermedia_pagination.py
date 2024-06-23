#!/usr/bin/env python3
"""
    Module implementing a function that computes start and end
    indices for pagination.

"""
import csv
import math
from typing import List, Dict


def index_range(page: int, page_size: int) -> tuple:
    """Computes start and end index for a pagination
    returns tuple
    """
    if page <= 0:
        raise ValueError("Page must be a positive integer")
    if page_size <= 0:
        raise ValueError("Page size must be a positive integer")
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular basy  names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a list of lists from popular baby names data"""
        assert isinstance(page, int) and page >\
            0, "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size >\
            0, "Page size must be a positive integer"
        start_index, end_index = index_range(page, page_size)

        data_set = self.dataset()

        if start_index >= len(data_set):
            return []
        return data_set[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, any]:
        """Returns a dictionary of hypermedia information"""
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        if page < total_pages:
            next_page = page + 1
        else:
            next_page = None
        if page > 1:
            prev_page = page - 1
        else:
            prev_page = None

        return {
                "page_size": len(data),
                "page": page,
                "data": data,
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": total_pages
                }
