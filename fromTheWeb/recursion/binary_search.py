def binary_search(arr, key):
    def helper(arr, key, low, high):
        if low > high: 
            return None
        mid = (low + high) // 2

        if arr[mid] == key:
            return (mid, key)

        if key > arr[mid]:
            return helper(arr, key, mid+1, high)
        else:
            return helper(arr, key, low, mid-1)
    return helper(arr,key,0,len(arr)-1)

def binary_search_while(arr, key):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low+high) // 2
        if arr[mid] == key:
            return (mid, key)
        if arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return None


print binary_search([1,2,3,4,5,6,7], 7)
# print binary_search_while([1,2,3,4,5,6,7], 9)