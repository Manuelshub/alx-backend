#!/usr/bin/env python3
"""
This module contains a function and a class.
"""
import csv
import math
from typing import List, Tuple, Dict


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
        """
        Retrieves a page of data from the dataset.

        Args:
            page (int): The page number to retrieve (1-indexed). Defaults to 1.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            List[List]: A list of lists containing the data for a page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        assert isinstance(self.dataset(), list)

        st_index, end_index = index_range(page, page_size)
        if page >= len(self.dataset()) or page_size == 0:
            return []

        return self.dataset()[st_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Retrieves hypermedia information for a page of data from the dataset.

        Args:
            page (int): The page number to retrieve (1-indexed). Defaults to 1.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            Dict: A dictionary containing hypermedia information for a page.
        """
        length = len(self.dataset())
        dataset = Server.get_page(self, page, page_size)
        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < math.ceil(length / page_size) else None
        total_pages = math.ceil(length / page_size)

        return {
            "page_size": page_size,
            "page": page,
            "data": dataset,
            "next_page": next_page,
            "page_page": prev_page,
            "total_pages": total_pages
        }
