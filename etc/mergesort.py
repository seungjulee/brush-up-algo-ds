def merge_sort(arr):
    def merge(arr, lowHalf, highHalf):
        # reinitialize arr
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

        merge_sort(lowHalf)
        merge_sort(highHalf)
        merge(arr, lowHalf, highHalf)

    return arr

arr = [5,34,-1,12,5,23,12]
print merge_sort(arr)
