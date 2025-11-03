def median(a, b, c):
    if b < a < c or b > a > c:
        return a
    elif a < b < c or a > b > c:
        return b
    else:
        return c

# this code snippet was referenced from discussion slides
def partition(arr, low, high):
    pivot = median(low, high, arr[(high + low)//2])
    up = low
    down = high
    while up < down:
        for i in range(up, high):
            if arr[up] > pivot:
                break
            up += 1
        for j in range(high, low, -1):
            if arr[down] < pivot:
                break
            down -= 1
        if up < down:
            arr[up], arr[down] = arr[down], arr[up]
            return down
    arr[low], arr[down] = arr[down], arr[low]
    return down

def quicksort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)