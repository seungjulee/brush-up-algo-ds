def search_item_in_1D_array(arr, target):
    first = 0
    last = len(arr)-1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if arr[mid] == target:
            found = True
            return found
        else:
            if target < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

def search_item_in_2D_array(arr, target):
    M = len(arr)
    N = len(arr[0])

    for j in range(M):
        if target > arr[j][N-1]:
            continue
        else:
            return search_item_in_1D_array(arr[j], target)
    return False

    # j = N // 2
    # while j >= 0 or j < M:
    #     if arr[j][0] < target < arr[j][N-1]:
    #         return search_item_in_1D_array(arr[j], target)
    #     elif arr[j][0] < target:
    #         j = j*

def binary_search(arr, target):
    found = False
    first = 0
    last = len(arr) - 1

    while first <= last and not found:
        mid = (first + last) // 2
        if arr[mid] == target:
            found = True
            return found
        else:
            if item < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

print search_item_in_2D_array([[1,2,3],[4,5,6],[7,8,9]], 10)