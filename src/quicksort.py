# This code snippet was referenced from discussion slides

def partition(arr, low, high, sortOrder):
    pivot = arr[low]
    up = low + 1
    down = high
    while up <= down:
        if sortOrder == "ascending":
            while up <= high and arr[up] < pivot:
                up += 1
            while arr[down] > pivot:
                down -= 1
        elif sortOrder == "descending":
            while up <= high and arr[up] > pivot:
                up += 1
            while arr[down] < pivot:
                down -= 1

        if up < down:
            arr[up], arr[down] = arr[down], arr[up]
            up += 1
            down -= 1
        elif up == down:
            break

    arr[low], arr[down] = arr[down], arr[low]
    return down

def quicksort(arr, low, high, sortOrder="descending"): #O(m^2)
    if low < high:
        p = partition(arr, low, high, sortOrder)
        quicksort(arr, low, p - 1, sortOrder)
        quicksort(arr, p + 1, high, sortOrder)