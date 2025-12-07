def quick_sort(arr):
    """
    Quick sort is a divide and conquer algorithm that selects a pivot element and partitions the array around the pivot such that
    elements smaller than the pivot are on the left and elements greater than the pivot are on the right. The process is repeated
    for the left and right subarrays.

    Time complexity: 

    WCS: O(n^2), where n is the number of elements in the array (pivot is the smallest or largest element)
    BCS: O(n log n), where n is the number of elements in the array

    Space complexity: O(log n)
    IN-PLACE
    NOT STABLE
    """
    def partition(arr, low, high):
        i = low - 1
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i + 1

    def quick_sort_helper(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)

            # Sort elements before and after partition
            quick_sort_helper(arr, low, pi - 1)
            quick_sort_helper(arr, pi + 1, high)

    quick_sort_helper(arr, 0, len(arr) - 1)
    return arr