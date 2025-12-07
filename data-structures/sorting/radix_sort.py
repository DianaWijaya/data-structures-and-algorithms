def radix_sort(arr):
    """
    Radix sort is a non-comparative sorting algorithm that sorts data with integer keys by grouping keys by the individual digits which
    share the same significant position and value.

    Time complexity: 

    WCS: O(nk), where n is the number of elements in the array and k is the number of digits in the largest element
    BCS: O(nk), where n is the number of elements in the array and k is the number of digits in the largest element

    Space complexity: O(n + k)
    NOT IN-PLACE
    STABLE
    """
    def counting_sort(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        # Store the count of each element
        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1

        # Change count[i] so that count[i] now contains the actual position of this element in the output array
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the output array
        i = n - 1
        while i >= 0:
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1

        # Copy the output array to arr, so that arr now contains the sorted elements
        for i in range(n):
            arr[i] = output[i]

    n = len(arr)
    max_element = max(arr)

    exp = 1
    while max_element // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

    return arr