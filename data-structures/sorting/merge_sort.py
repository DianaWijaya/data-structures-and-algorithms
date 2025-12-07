def merge_sort(arr):
    """
    Merge sort is a divide and conquer algorithm that divides the input array into two halves, calls itself for the two halves, 
    and then merges the two sorted halves.

    Time complexity: 

    WCS: O(n log n), where n is the number of elements in the array
    BCS: O(n log n), where n is the number of elements in the array

    Space complexity: O(n)
    NOT IN-PLACE
    STABLE
    """
    def merge(arr, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid

        # Create temporary arrays
        L = [0] * n1
        R = [0] * n2

        # Copy data to temporary arrays L[] and R[]
        for i in range(n1):
            L[i] = arr[left + i]

        for j in range(n2):
            R[j] = arr[mid + 1 + j]

        # Merge the temporary arrays back into arr[left..right]
        i = 0
        j = 0
        k = left

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy the remaining elements of L[], if there are any
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        # Copy the remaining elements of R[], if there are any
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def merge_sort_helper(arr, left, right):
        if left < right:
            mid = left + (right - left) // 2

            # Sort first and second halves
            merge_sort_helper(arr, left, mid)
            merge_sort_helper(arr, mid + 1, right)

            # Merge the sorted halves
            merge(arr, left, mid, right)

    merge_sort_helper(arr, 0, len(arr) - 1)
    return arr