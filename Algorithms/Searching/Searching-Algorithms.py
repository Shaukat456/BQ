# Linear Search
# Real-world analogy: Finding a specific book in a stack of unsorted books by checking each one sequentially.
# Example: Searching for a specific number in an unsorted list.
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Use case: Linear search is useful when dealing with small datasets or when the list is unsorted.


# Binary Search
# Real-world analogy: Looking for a word in a dictionary by opening to the middle and determining if the word is in the first or second half, then repeating the process.
# Example: Searching for a specific number in a sorted list.
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Use case: Binary search is efficient for large datasets but requires the list to be sorted.

# Jump Search
# Real-world analogy: Searching for a name in a telephone directory by jumping ahead by fixed steps and then doing a linear search within the block.
# Example: Searching for a specific number in a sorted list by jumping ahead by fixed steps.
import math


def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1


# Use case: Jump search is useful for large sorted datasets where binary search might be too slow.


# Interpolation Search
# Real-world analogy: Searching for a specific page in a book by estimating the position based on the page numbers.
# Example: Searching for a specific number in a uniformly distributed sorted list.
def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))
        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1


# Use case: Interpolation search is efficient for large uniformly distributed sorted datasets.


# Exponential Search
# Real-world analogy: Finding a specific chapter in a book by doubling the number of pages you skip each time until you find the chapter.
# Example: Searching for a specific number in a sorted list by doubling the range each time.
def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
    return binary_search(arr[: min(i, len(arr))], target)


# Use case: Exponential search is useful for unbounded or infinite lists where the size of the list is unknown.
