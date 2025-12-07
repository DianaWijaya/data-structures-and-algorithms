from __future__ import annotations
from typing import TypeVar

T = TypeVar("T")

def binary_search(l: list[T], item: T) -> int:
    """
    Utilize the binary search algorithm to find the index where a particular element would be stored.

    Args:
    - l: the list to find the element from
    - item: the item to be searched from the list

    Returns:
    - the index at which either this item is located or where this item would be inserted preserve the
      ordering

    Complexity:
    - Worst Case: O(log(N)), where N is the length of l.
    - Best Case: O(1), which occurs when middle index contains item.
    """

    return _binary_search_aux(l, item, 0, len(l))

def _binary_search_aux(l: list[T], item: T, lo: int, hi: int) -> int:
    """
    Auxilliary method used by binary search.

    Args:
    - l: the list to search the element from
    - item: the element to be searched from the list
    - lo: smallest index where the return value could be
    - hi: largest index where the return value cold be

    Returns:
    - the index where this item is located in, only if it already exists in the list

    Complexity:
    - Worst case: O(log(N)), where N is the length of l.
    - Best case: O(1), which occurs when middle index contains item.
    """

    if lo == hi:
        return lo
    mid = (hi + lo) // 2
    if l[mid] > item:
        # Item would be before mid
        return _binary_search_aux(l, item, lo, mid)
    elif l[mid] < item:
        # Item would be after mid
        return _binary_search_aux(l, item, mid+1, hi)
    elif l[mid] == item:
        return mid
    raise ValueError(f"Comparison operator poorly implemented {item} and {l[mid]} cannot be compared.")