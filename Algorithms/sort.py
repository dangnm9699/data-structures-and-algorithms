from typing import List


def selection_sort(arr: List[int]):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def bubble_sort(arr: List[int]):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


def insertion_sort(arr: List[int]):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge_sort(arr: List[int]):
    n = len(arr)
    if n > 1:
        # Finding middle index of array
        mid = n // 2
        # Divide array into 2 halves
        _low = arr[:mid]
        _high = arr[mid:]
        # Sort left half
        merge_sort(_low)
        # Sort right half
        merge_sort(_high)
        # Merge 2 halves into 1
        _merge(arr, _low, _high)


def _merge(arr: List[int], _low: List[int], _high: List[int]):
    # Initialize
    # i: current index of left half
    # j: current index of right half
    # k: current index of merged one
    i = j = k = 0
    # Copy from 2 halves into merged one util one index exceeds limit
    while i < len(_low) and j < len(_high):
        if _low[i] < _high[j]:
            arr[k] = _low[i]
            i += 1
        else:
            arr[k] = _high[j]
            j += 1
        k += 1
    # Check if another index exceeds limit
    while i < len(_low):
        arr[k] = _low[i]
        i += 1
        k += 1
    while j < len(_high):
        arr[k] = _high[j]
        j += 1
        k += 1


def quick_sort(arr: List[int]):
    pass


def heap_sort(arr: List[int]):
    pass
