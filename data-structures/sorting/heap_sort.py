def heap_sort(arr):
    """
    Heap sort is a comparison-based sorting technique based on Binary Heap data structure. It is similar to selection sort 
    where we first find the maximum element and place the maximum element at the end. We repeat the same process for the 
    remaining elements.

    Time complexity: 

    WCS: O(n log n), where n is the number of elements in the array
    BCS: O(n log n), where n is the number of elements in the array

    Space complexity: O(1)
    IN-PLACE
    NOT STABLE
    """
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # Check if the left child of the root exists and is greater than the root
        if left < n and arr[i] < arr[left]:
            largest = left

        # Check if the right child of the root exists and is greater than the root
        if right < n and arr[largest] < arr[right]:
            largest = right

        # Change the root if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]

            # Heapify the root
            heapify(arr, n, largest)

    n = len(arr)

    # Build a maxheap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr