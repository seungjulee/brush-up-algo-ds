from sys import maxint
def mergesort(arr):
    def merge(arr, lowHalf, highHalf):
        del arr[:]

        while lowHalf and highHalf:
            if lowHalf[0] < highHalf[0]:
                arr.append(lowHalf.pop(0))
            else:
                arr.append(highHalf.pop(0))

        eitherHalf = lowHalf or highHalf

        while eitherHalf:
            arr.append(eitherHalf.pop(0))

    if len(arr) > 1:
        mid = len(arr) // 2
        lowHalf = arr[:mid]
        highHalf = arr[mid:]
        mergesort(lowHalf)
        mergesort(highHalf)
        merge(arr,lowHalf,highHalf)

    return arr

def quicksort(arr):
    def partition(arr, low, high):
        pivot_idx = low
        compare_idx = high

        for j in xrange(low, high+1):
            if arr[j] < arr[compare_idx]:
                arr[j], arr[pivot_idx] = arr[pivot_idx], arr[j]
                pivot_idx += 1

        arr[pivot_idx], arr[compare_idx] = arr[compare_idx], arr[pivot_idx]

        return compare_idx

    def quicksort_helper(arr, low, high):
        if (low < high):
            pivot = partition(arr, low, high)
            quicksort_helper(arr, low, pivot - 1)
            quicksort_helper(arr, pivot + 1, high)
        return arr

    return quicksort_helper(arr, 0, len(arr) - 1)

def  closestNumbers( l,  s):
    s = map(int, s.split())
    N = len(s)
    if N == 0:
        raise "Input Required"
    if N == 1:
        return s[0]
    if N == 2:
        return abs(s[0]-s[1])

    mergesort(s)

    shortest_dist = abs(s[0]-s[1])
    res_str = ""
    shortest_arr = [s[0], s[1]]
    for i in xrange(N-1):
        if abs(s[i]-s[i+1]) < shortest_dist:
            shortest_arr = []
            shortest_arr.push(s[i]); shortest_arr.push(s[i+1])
            shortest_dist = abs(s[i]-s[i+1])
        elif abs(s[i]-s[i+1]) == shortest_dist:
            shortest_arr.push(s[i]); shortest_arr.push(s[i+1])

    # for i in xrange(N-1):
    #     if abs(s[i]-s[i+1]) == shortest_dist:
    #         res_str += "%s %s " % (s[i], s[i+1])
    return res_str

