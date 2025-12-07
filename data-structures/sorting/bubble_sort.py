def bubble_sort(arr):
    """
    Goes through the list and compares each element with the next element. If the current element is greater than the next 
    element, the elements are swapped. This process is repeated until the list is sorted.

    Time complexity: 
    WCS: O(n^2), where n is the number of elements in the array (list is in reverse)
    BCS: O(n), where n is the number of elements in the array (list is sorted)

    Space complexity: O(1)
    IN-PLACE
    STABLE
    """
    n = len(arr)
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # If the element found is greater than the next element
            if arr[j] > arr[j+1]:

                # Flip the elements
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr