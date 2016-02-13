def find_min(arr):
    def find_min_helper(arr, low, high):
        if high < low:
            return arr[0]
        if high == low:
            return arr[low]

        mid = (low+high) // 2

        if mid < high and arr[mid+1] < arr[mid]:
            return arr[mid+1]
        # [6,5,4,1,2,3]
        if mid > low and arr[mid] < arr[mid-1]:
            return arr[mid]
        
        if arr[high] > arr[mid]:
            return find_min_helper(arr,low, mid-1)
        else:
            return find_min_helper(arr,mid+1,high)
    return find_min_helper(arr, 0, len(arr)-1)




print find_min([5,4,1,2,3])