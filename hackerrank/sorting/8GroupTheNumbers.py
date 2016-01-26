def groupNumbers(arr):
    def isEven(num):
        return num % 2 == 0

    start = 0
    end = len(arr) - 1
    compare_idx = end
    pivot_idx = start
    compare_isEven = isEven(arr[compare_idx])

    for j in xrange(start, end+1):
        if isEven(arr[j]):
            arr[j], arr[pivot_idx] = arr[pivot_idx], arr[j]
            pivot_idx += 1 

    arr[compare_idx], arr[pivot_idx] = arr[pivot_idx], arr[compare_idx]


if __name__ == "__main__":
    arr = [5,1,3,5,4,6]
    print "BEFORE", arr
    groupNumbers(arr)
    print "AFTER", arr