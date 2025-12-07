from __future__ import annotations
from typing import TypeVar

T = TypeVar("T")

def merge(l1: list[T], l2: list[T], key=lambda x:x) -> list[T]:
    """
    Merges two sorted lists into one larger sorted list, containing all elements from the smallers lists. The 'key' kwarg allows 
    you to define s custom sorting order.

    Args:
    - l1: the first list
    - l2: the second list
    - key: The key for comparing

    Returns:
    - new_list: the list that is sorted

    Complexity:
    - Worst case: O(n * comp(T)), where n is (len(l1)+len(l2)), where l1 is the first list and l2 is the second list. Then, 
      comp(T) is the complexity of the comparison.
    - Best case: O(n * comp(T)), where n is (len(l1)+len(l2)), where l1 is the first list and l2 is the second list. Then, 
      comp(T) is the complexity of the comparison.
    """
    
    new_list = [] # O(1)
    cur_left = 0 # O(1)
    cur_right = 0 # O(1)
    while cur_left < len(l1) and cur_right < len(l2): # O(n)
        if key(l1[cur_left]) <= key(l2[cur_right]): # O(comp(T))
            new_list.append(l1[cur_left]) # O(1)
            cur_left += 1 # O(1)
        else: # O(1)
            new_list.append(l2[cur_right]) # O(1)
            cur_right += 1 # O(1)
    new_list += l1[cur_left:] # O(1)
    new_list += l2[cur_right:] # O(1)
    return new_list # O(1)

def mergesort(l: list[T]) -> list[T]:
    """
    Sort a list using mergesort operation.

    Args:
    - l: the list

    Returns:
    - the sorted list

    Complexity:
    - Worst case: O(NlogN * comp(T)), where n is the number of elements in the array and comp(T) is the complexity of the 
      comparison. In this case, comp(T) is considered O(1).
    - Best case: O(NlogN * comp(T)), where n is the number of elements in the array and comp(T) is the complexity of the 
      comparison. In this case, comp(T) is considered O(1).
    """

    if len(l) <= 1: 
        return l 
    break_index = (len(l)+1) // 2 
    l1 = mergesort(l[:break_index])
    l2 = mergesort(l[break_index:])
    return merge(l1, l2)
