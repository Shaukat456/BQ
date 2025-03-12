def bubble_sort(arr):
    """
    Bubble Sort:
    - Repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.
    - The pass through the list is repeated until the list is sorted.

    Steps:
    1. Start with the first element.
    2. Compare the current element with the next element.
    3. If the current element is greater than the next element, swap them.
    4. Move to the next element and repeat the process until the end of the list.
    5. Repeat the entire process for the remaining elements.

    Example Output:
    Original array: [64, 34, 25, 12, 22, 11, 90]
    Sorted array with Bubble Sort: [11, 12, 22, 25, 34, 64, 90]

    When to use:
    - Simple to implement.
    - Useful for small datasets or nearly sorted datasets.
    - Not efficient for large datasets.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def selection_sort(arr):
    """
    Selection Sort:
    - Divides the input list into two parts: the sublist of items already sorted and the sublist of items remaining to be sorted.
    - Repeatedly selects the smallest (or largest) element from the unsorted sublist and moves it to the sorted sublist.

    Steps:
    1. Start with the first element as the minimum.
    2. Compare the current minimum with the next element.
    3. If the next element is smaller, update the minimum.
    4. After completing the pass, swap the minimum element with the first unsorted element.
    5. Repeat the process for the remaining elements.

    Example Output:
    Original array: [64, 34, 25, 12, 22, 11, 90]
    Sorted array with Selection Sort: [11, 12, 22, 25, 34, 64, 90]

    When to use:
    - Simple to implement.
    - Useful for small datasets.
    - Not efficient for large datasets.
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def insertion_sort(arr):
    """
    Insertion Sort:
    - Builds the final sorted array one item at a time.
    - Takes each element from the input and finds the appropriate location within the sorted part of the array.

    Steps:
    1. Start with the second element as the key.
    2. Compare the key with the elements before it.
    3. Shift all elements greater than the key to the right.
    4. Insert the key at the correct position.
    5. Repeat the process for the remaining elements.

    Example Output:
    Original array: [64, 34, 25, 12, 22, 11, 90]
    Sorted array with Insertion Sort: [11, 12, 22, 25, 34, 64, 90]

    When to use:
    - Simple to implement.
    - Efficient for small datasets or nearly sorted datasets.
    - More efficient than Bubble Sort and Selection Sort for small datasets.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def quick_sort(arr):
    """
    Quick Sort:
    - Selects a 'pivot' element from the array and partitions the other elements into two sub-arrays, according to whether they are less than or greater than the pivot.
    - Recursively applies the same logic to the sub-arrays.

    Steps:
    1. Pick a pivot element.
    2. Partition the array into two sub-arrays: elements less than the pivot and elements greater than the pivot.
    3. Recursively apply the above steps to the sub-arrays.
    4. Combine the sub-arrays to get the sorted array.

    Example Output:
    Original array: [64, 34, 25, 12, 22, 11, 90]
    Sorted array with Quick Sort: [11, 12, 22, 25, 34, 64, 90]

    When to use:
    - Efficient for large datasets.
    - Average-case time complexity is O(n log n).
    - Worst-case time complexity is O(n^2), but this can be mitigated with good pivot selection.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr):
    """
    Merge Sort:
    - Divides the array into two halves, sorts them and then merges them.

    Steps:
    1. Divide the array into two halves.
    2. Recursively sort each half.
    3. Merge the two sorted halves to produce the sorted array.

    Example Output:
    Original array: [64, 34, 25, 12, 22, 11, 90]
    Sorted array with Merge Sort: [11, 12, 22, 25, 34, 64, 90]

    When to use:
    - Efficient for large datasets.
    - Time complexity is O(n log n) in all cases.
    - Requires additional space for merging.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Example usage:
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    print("Original array:", arr)

    bubble_sort(arr)
    print("Sorted array with Bubble Sort:", arr)

    arr = [64, 34, 25, 12, 22, 11, 90]
    selection_sort(arr)
    print("Sorted array with Selection Sort:", arr)

    arr = [64, 34, 25, 12, 22, 11, 90]
    insertion_sort(arr)
    print("Sorted array with Insertion Sort:", arr)

    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = quick_sort(arr)
    print("Sorted array with Quick Sort:", sorted_arr)

    arr = [64, 34, 25, 12, 22, 11, 90]
    merge_sort(arr)
    print("Sorted array with Merge Sort:", arr)

    # Additional example usage
    arr = [5, 3, 8, 4, 2]
    print("\nOriginal array:", arr)
