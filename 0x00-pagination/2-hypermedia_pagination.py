#!/usr/bin/env python3
"""
Module for hypermedia pagination
"""

import csv
import math
from typing import List
from typing import Tuple
from typing import Dict

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of start and end indexes for pagination.

    Args:
        page (int): The page number, 1-indexed.
        page_size (int): The size of each page.

    Returns:
        tuple: A tuple containing the start index and end index for the given page.
    """
    assert isinstance(page, int) and page > 0, "Page must be a positive integer"
    assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index

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
        """
        Return the requested page of the dataset.

        Args:
            page (int): The page number, 1-indexed. Defaults to 1.
            page_size (int): The size of each page. Defaults to 10.

        Returns:
            List[List]: The requested page of the dataset.
        """
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Return hypermedia pagination information.

        Args:
            page (int): The page number, 1-indexed. Defaults to 1.
            page_size (int): The size of each page. Defaults to 10.

        Returns:
            Dict: A dictionary containing hypermedia pagination information.
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

