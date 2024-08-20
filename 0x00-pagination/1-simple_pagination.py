#!/usr/bin/env python3
"""
This module contains a function and a class.
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Function that returns a tuple of size two

    Args:
        page: the number of the current page.
        page_size: the total number of pages

    Return:
        A tuple of size two containing a start index and an end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)

class Server:
    """Server class to paginate a database of popular baby names
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
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
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        assert isinstance(self.dataset(), list)

        st_index, end_index = index_range(page, page_size)
        if page >= len(self.dataset()) or page_size == 0:
            return []
        
        return self.dataset()[st_index:end_index]
