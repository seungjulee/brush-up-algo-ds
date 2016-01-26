def mergeSort(arr):
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

        mergeSort(lowHalf)
        mergeSort(highHalf)

        merge(arr, lowHalf, highHalf)

if __name__ == "__main__":
    arr = [2,3,3,3,2,1,5,6,6,2]
    print "Before: ", arr
    mergeSort(arr)
    print "After: ", arr

