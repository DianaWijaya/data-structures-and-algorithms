def counting_sort(arr):
    """
    Counting sort is a sorting technique based on keys between a specific range. It works by counting the number of objects having
    distinct key values (kind of hashing). Then doing some arithmetic to calculate the position of each object in the output sequence.

    Time complexity: 

    WCS: O(n + k), where n is the number of elements in the array and k is the range of the non-negative key values
    BCS: O(n + k), where n is the number of elements in the array and k is the range of the non-negative key values

    Space complexity: O(n + k)
    NOT IN-PLACE
    STABLE
    """
    n = len(arr)
    output = [0] * n

    # Find the maximum element in the array
    max_element = max(arr)

    # The output array that will have sorted arr
    count = [0] * (max_element + 1)

    # Store the count of each element
    for i in range(n):
        count[arr[i]] += 1

    # Change count[i] so that count[i] now contains the actual position of this element in the output array
    for i in range(1, max_element + 1):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    # Copy the output array to arr, so that arr now contains the sorted elements
    for i in range(n):
        arr[i] = output[i]

    return arr