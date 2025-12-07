def insertion_sort(arr):
    """
    Goes through the list and compares the current element with the largest element on the left. If the current element is smaller
    than the largest element on the left, the largest element is moved one position to the right. This process is repeated until the
    list is sorted.

    Time complexity: 

    WCS: O(n^2), where n is the number of elements in the array (list is in reverse)
    BCS: O(n), where n is the number of elements in the array (list is sorted)

    Space complexity: O(1)
    IN-PLACE
    STABLE
    """
    n = len(arr)
    for i in range(1, n):

        # Current element to be compared 
        current = arr[i]

        # Compare the current element with the largest element on the left
        j = i - 1
        while j >= 0 and current < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        # Move the current element to its correct position
        arr[j+1] = current

    return arr