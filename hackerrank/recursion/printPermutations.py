def print_permutations(arr):
    def print_permutations_recursive(arr, i):
        if i == len(arr):
            print arr
            return

        for j in xrange(i, len(arr)):
            # print "Before Swap 1:", arr, i, j
            arr[i], arr[j] = arr[j], arr[i]
            # print "After Swap 1:", arr, i, j
            print_permutations_recursive(arr, i+1)
            # print "Before Swap 2:", arr, i, j
            arr[i], arr[j] = arr[j], arr[i]
            # print "After Swap 2:", arr, i, j
    return print_permutations_recursive(arr, 0)

print_permutations(['a','b','c'])