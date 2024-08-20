#!/usr/bin/env python3
"""
This module contains a simple helper function
"""
from typing import Tuple


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
