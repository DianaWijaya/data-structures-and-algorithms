def quick_select(arr, k):
    """
    Quick select is a selection algorithm that finds the kth smallest element in an unordered list. The algorithm selects a pivot
    element and partitions the array around the pivot such that elements smaller than the pivot are on the left and elements greater
    than the pivot are on the right. The process is repeated for the left or right subarray depending on the position of the pivot.

    Time complexity: 

    WCS: O(n^2), where n is the number of elements in the array (pivot is the smallest or largest element)
    BCS: O(n), where n is the number of elements in the array, when the pivot is the median of the array

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

    def quick_select_helper(arr, low, high, k):
        if low < high:
            pi = partition(arr, low, high)

            # If the position of the pivot is the same as k
            if pi == k:
                return arr[pi]

            # If the position of the pivot is greater than k
            elif pi > k:
                return quick_select_helper(arr, low, pi - 1, k)

            # If the position of the pivot is smaller than k
            else:
                return quick_select_helper(arr, pi + 1, high, k)

    return quick_select_helper(arr, 0, len(arr) - 1, k)
