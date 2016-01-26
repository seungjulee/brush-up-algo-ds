def divideAndConquer(iArray):
    if left < right:
        return
    
    mid = N/2

    n.data = iArray[mid]
    
    n.left = divideAndConquer(iArray[mid:])
    n.right = divideAndConquer(iArray[:mid])
    
    return n

print divideAndConquer([0,2,3,4,5])