from typing import List


def bubble_sort(arr: List[int]):
    """
    Bubble sort for an integer array
    :param arr: array of integer elements
    :return: sorted array order by ascending
    """
    n = len(arr)
    if n < 2:
        return arr
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def selection_sort(arr: List[int]):
    """
    Selection sort for an integer array
    :param arr: array of integer elements
    :return: sorted array order by ascending
    """
    n = len(arr)
    if n < 2:
        return arr
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr: List[int]):
    """
    Merge sort for an integer array
    :param arr: array of integer elements
    :return: sorted array order by ascending
    """
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
    return arr


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
    pass
