def swap(arr, i, j):
    arr[j], arr[i] = arr[i], arr[j]

def partition(arr, start, end, pivot):
    i = start
    j = start
    doneEqual = False
    while j < end:
    # for j in xrange(start, end): <- doesn't work
        if arr[j] < pivot:
            swap(arr,i,j)
            i += 1
        elif arr[j] == pivot and not doneEqual:
            swap(arr,j,end)
            j -= 1
            doneEqual = True
        j += 1

    swap(arr, i, end)
    return i

def sortNutsAndBolts(nuts, bolts, start, end):
    if start < end:
        pivot = partition(nuts, start, end, bolts[end])
        partition(bolts, start, end, nuts[pivot])
        sortNutsAndBolts(nuts, bolts, start, pivot-1)
        sortNutsAndBolts(nuts, bolts, pivot+1, end)


def main():
    inArr = [[3,2,1,4],[4,2,3,1]]
    sortNutsAndBolts(inArr[0], inArr[1], 0, len(inArr[0])-1)
    # expected out (in any order)
    #[[N1,B1],[N2,B2]...]
    print inArr[0]
    print inArr[1]

if __name__ == "__main__":
    main()