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


def quick_sort(arr: List[int], lo=None, hi=None):
    if lo is None:
        lo = 0
    if hi is None:
        hi = len(arr) - 1
    if lo < hi:
        pi = _partition_lomuto(arr, lo, hi)
        quick_sort(arr, lo, pi - 1)
        quick_sort(arr, pi + 1, hi)


def _partition_lomuto(arr: List[int], lo: int, hi: int):
    pivot = arr[hi]
    i = lo
    for j in range(lo, hi):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[hi] = arr[hi], arr[i]
    return i


def _partition_hoare(arr: List[int], lo: int, hi: int):
    pivot = arr[(lo + hi) // 2]
    i = lo
    j = hi
    while True:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


def heap_sort(arr: List[int]):
    pass
