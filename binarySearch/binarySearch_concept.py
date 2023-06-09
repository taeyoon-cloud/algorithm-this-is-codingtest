import sys

input_data = sys.stdin.readline().rstrip()

def binary_search_recursion(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search_recursion(array, target, start, mid - 1)
    else:
        return binary_search_recursion(array, target, mid + 1, end)
    

def binary_search_loop(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

