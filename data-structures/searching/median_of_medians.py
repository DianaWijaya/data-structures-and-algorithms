def median_of_medians(arr, k):
    """
    Median of medians is a selection algorithm that finds the kth smallest element in an unordered list. The algorithm divides the
    list into sublists of size 5, finds the median of each sublist, and then recursively finds the median of the medians until the
    kth smallest element is found.

    Time complexity: 

    WCS: O(n), where n is the number of elements in the array
    BCS: O(n), where n is the number of elements in the array

    Space complexity: O(n)
    NOT IN-PLACE
    STABLE
    """
    def partition(arr, left, right, pivot_index):
        pivot_value = arr[pivot_index]
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        store_index = left

        for i in range(left, right):
            if arr[i] < pivot_value:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1

        arr[right], arr[store_index] = arr[store_index], arr[right]
        return store_index

    def select(arr, left, right, k):
        if left == right:
            return arr[left]

        pivot_index = left
        while True:
            pivot_index = partition(arr, left, right, pivot_index)
            if k == pivot_index:
                return arr[k]
            elif k < pivot_index:
                right = pivot_index - 1
            else:
                left = pivot_index + 1

    n = len(arr)
    return select(arr, 0, n - 1, k)