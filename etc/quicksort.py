def quicksort(arr):
    def partition(arr, start, end):
        if start < end:
            compare_idx = end

            pivot_idx = start
            for j in xrange(start, end+1):
                if arr[j] < arr[compare_idx]:
                    arr[pivot_idx], arr[j] = arr[j], arr[pivot_idx]
                    pivot_idx += 1

            arr[pivot_idx], arr[compare_idx] = arr[compare_idx], arr[pivot_idx]

            return pivot_idx

    def quicksort_helper(arr, start, end):
        if start < end:
            pivot = partition(arr, start, end)
            quicksort_helper(arr, start, pivot-1)
            quicksort_helper(arr, pivot+1, end)

    quicksort_helper(arr, 0, len(arr)-1)

arr = [5,4,3,2,6,1]
print "BEFORE", arr
quicksort(arr)
print "AFTER", arr
    