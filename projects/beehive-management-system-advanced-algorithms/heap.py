"""Max Heap implemented using an array"""
from __future__ import annotations
__author__ = "Brendon Taylor, modified by Jackson Goerner"
__docformat__ = 'reStructuredText'

from typing import Generic
from referential_array import ArrayR, T


class MaxHeap(Generic[T]):
    MIN_CAPACITY = 1

    def __init__(self, max_size: int, an_array: ArrayR[T] = None, verbose=False) -> None:
        """
        If an_array is specified then the elements of the future 
        heap are known in advance.
        Assume that max_size=len(an_array) if given.

        O(1): initialization
        """
        if an_array is None:
            self.length = 0 
        else:
            self.length = max_size = len(an_array) 
        
        self.the_array = ArrayR(max(self.MIN_CAPACITY, max_size) + 1)

        if an_array:
            self.heapify(an_array, verbose)

    def __len__(self) -> int:
        """
        O(1): calculates the length of the ArrayR
        """
        return self.length

    def is_full(self) -> bool:
        """
        O(1): calculates the length added by 1 and compared to the length of the ArrayR
        """
        return self.length + 1 == len(self.the_array)
    
    def heapify(self, an_array: ArrayR[T], verbose: bool = False) -> None:
        """
        Apply bottom-up heap construction in O(n) time.

        O(n)
        """
        for i in range(self.length) :
            self.the_array[i+1] = an_array[i]
        for i in range(self.length//2, 0, -1) :
            self.sink(i)

    def rise(self, k: int) -> None:
        """
        Rise element at index k to its correct position
        :pre: 1 <= k <= self.length

        BCS: O(1): when element k is at the correct position, no swaps are done
        WCS: O(log n): where n is the number of elements in the heap, occurs when the element at 
             index k is swapped
        """
        item = self.the_array[k]
        while k > 1 and item > self.the_array[k // 2]:
            self.the_array[k] = self.the_array[k // 2]
            k = k // 2
        self.the_array[k] = item

    def add(self, element: T) -> bool:
        """
        Swaps elements while rising

        BCS: O(1), when the element is added to the end of the heap, and no swap is needed in rise
        WCS: O(log n), where n is the number of elements in the heap, occurs when the element at
             index k is swapped, due to the wrong position of the element
        """
        if self.is_full():
            raise IndexError

        self.length += 1
        self.the_array[self.length] = element
        self.rise(self.length)

    def largest_child(self, k: int) -> int:
        """
        Returns the index of k's child with greatest value.
        :pre: 1 <= k <= self.length // 2

        O(1): compares the two children of k and returns the index of the largest child
        """
        
        if 2 * k == self.length or \
                self.the_array[2 * k] > self.the_array[2 * k + 1]:
            return 2 * k
        else:
            return 2 * k + 1

    def sink(self, k: int) -> None:
        """ Make the element at index k sink to the correct position.
            :pre: 1 <= k <= self.length
            :complexity: ???

        BCS: O(1), when the element at index k is at the correct position, no swaps are done
        WCS: O(log n), where n is the number of elements in the heap, occurs when the element at
             index k is swapped, due to the wrong position of the element
        """
        item = self.the_array[k]

        while 2 * k <= self.length:
            max_child = self.largest_child(k)
            if self.the_array[max_child] <= item:
                break
            self.the_array[k] = self.the_array[max_child]
            k = max_child

        self.the_array[k] = item
        
    def get_max(self) -> T:
        """ 
        Remove (and return) the maximum element from the heap. 

        BCS: O(1), when the element at index 1 is the maximum element, and no swaps are done in sink
        WCS: O(log n), where n is the number of elements in the heap, occurs when the element at
        """
        if self.length == 0:
            raise IndexError

        max_elt = self.the_array[1]
        self.length -= 1
        if self.length > 0:
            self.the_array[1] = self.the_array[self.length+1]
            self.sink(1)
        return max_elt

if __name__ == '__main__':
    items = [ int(x) for x in input('Enter a list of numbers: ').strip().split(",") ]
    heap = MaxHeap(len(items))

    for item in items:
        heap.add(item)
        
    while(len(heap) > 0):
        print(heap.get_max())
