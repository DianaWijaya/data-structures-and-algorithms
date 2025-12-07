def binary_search(arr, target):
    """
    Binary search is a search algorithm that finds the position of a target value within a sorted array. The algorithm compares the
    target value to the middle element of the array. If the target value is equal to the middle element, the position is returned.
    If the target value is less than the middle element, the search continues in the lower half of the array. If the target value is
    greater than the middle element, the search continues in the upper half of the array. This process is repeated until the target
    value is found or the subarray is empty.

    Time complexity: 

    WCS: O(log n), where n is the number of elements in the array (element not found or placed at a corner of the array)
    BCS: O(1), where n is the number of elements in the array (element is in the middle of the array)
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Check if the target is in the middle
        if arr[mid] == target:
            return mid

        # If the target is greater than the middle element, ignore the left half
        elif arr[mid] < target:
            left = mid + 1

        # If the target is smaller than the middle element, ignore the right half
        else:
            right = mid - 1

    return -1