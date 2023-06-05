arr = [3, 1, 5, 6, 4, 7, 9, 8]


def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


def insertionSort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break

    return arr

def quickSort(arr, start, end):
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    quickSort(arr, start, right - 1)
    quickSort(arr, right + 1, end)

    return arr



def quickSortPython(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    tail = arr[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quickSort(left_side) + [pivot] + quickSort(right_side)


def countSort(arr):
    count = [0] * (max(arr) + 1)

    for i in range(len(arr)):
        count[arr[i]] += 1

    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end = ' ')


countSort(arr)    