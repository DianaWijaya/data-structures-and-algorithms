def selection_sort(arr):
    """
    Goes through the list and finds the minimum element in the unsorted part of the list. The minimum element is then swapped
    with the first element of the unsorted part. This process is repeated until the list is sorted.

    Time complexity: 
    WCS: O(n^2), where n is the number of elements in the array (list is in reverse)
    BCS: O(n^2), where n is the number of elements in the array (list is sorted)

    Space complexity: O(1)
    IN-PLACE
    NOT STABLE
    """
    n = len(arr)
    for i in range(n):

        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr