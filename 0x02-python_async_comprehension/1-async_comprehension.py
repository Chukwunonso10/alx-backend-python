#!/usr/bin/env python3
"""Getting a list from an async comprehension"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """retrieves async generated list and return it"""
    return [_ async for _ in async_generator()]
