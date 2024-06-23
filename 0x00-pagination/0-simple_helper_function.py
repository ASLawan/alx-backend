#!/usr/bin/env python3
"""
    Module implementing a function that computes start and end
    indices for pagination.

"""


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
