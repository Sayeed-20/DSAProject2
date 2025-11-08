def median(a, b, c):
    if b < a < c or b > a > c:
        return a
    elif a < b < c or a > b > c:
        return b
    else:
        return c

# this code snippet was referenced from discussion slides
def partition(arr, low, high, sortOrder):
    pivot = median(arr[low], arr[(high + low)//2], arr[high])
    up = low
    down = high
    while up < down:
        if sortOrder == "ascending":
            for i in range(up, high):
                if arr[up] >= pivot:
                    break
                up += 1
            for j in range(high, low, -1):
                if arr[down] <= pivot:
                    break
                down -= 1
        elif sortOrder == "descending":
            for i in range(up, high):
                if arr[up] <= pivot:
                    break
                up += 1
            for j in range(high, low, -1):
                if arr[down] >= pivot:
                    break
                down -= 1

        if up < down:
            arr[up], arr[down] = arr[down], arr[up]


    arr[low], arr[down] = arr[down], arr[low]
    return down

def quicksort(arr, low, high, sortOrder="descending"):
    if low < high:
        p = partition(arr, low, high, sortOrder)
        quicksort(arr, low, p - 1, sortOrder)
        quicksort(arr, p + 1, high, sortOrder)