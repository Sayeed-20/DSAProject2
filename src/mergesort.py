# The implementation for mergesort was referenced from the slides

# Merge two subarrays from arr
def merge(arr, left, mid, right, sortOrder):
    # Create X = arr[left..mid] & Y = arr[mid+1..right]
    X = arr[left : mid + 1]
    Y = arr[mid + 1 : right + 1]

    n1 = len(X)
    n2 = len(Y)

    # Merge the arrays X and Y into arr
    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if sortOrder == 'descending':
            if X[i] >= Y[j]:
                arr[k] = X[i]
                i += 1
            else:
                arr[k] = Y[j]
                j += 1
            k += 1
        elif sortOrder == 'ascending':
            if X[i] <= Y[j]:
                arr[k] = X[i]
                i += 1
            else:
                arr[k] = Y[j]
                j += 1
            k += 1

    # When we run out of elements in either X or Y append the remaining elements
    while i < n1:
        arr[k] = X[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = Y[j]
        j += 1
        k += 1

def mergeSort(arr, left, right, sortOrder="descending"): #O(mlogm)
    if left < right:
        # m is the point where the array is divided into two subarrays
        mid = (left + right) // 2
        mergeSort(arr, left, mid, sortOrder)
        mergeSort(arr, mid + 1, right, sortOrder)

        # Merge the sorted subarrays
        merge(arr, left, mid, right, sortOrder)