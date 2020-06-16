def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
            


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    mid = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        # checking if target is greater
        elif arr[mid] < target:
            low = mid + 1
        # else if target is less than mid
        elif arr[mid] > target:
            high = mid - 1

    return -1  # not found
