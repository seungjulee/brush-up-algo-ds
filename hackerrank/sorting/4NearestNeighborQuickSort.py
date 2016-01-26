from math import sqrt 
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __repr__(self):
        return "(%s, %s)" % (self.x, self.y)

def partition(arr, low, high, rootPt, K):
    if low < high:
        compIdx = high
        pivotIdx = low

        for j in xrange(low, high+1):
            if rootPt - arr[j] < rootPt - arr[compIdx]:
                arr[j], arr[pivotIdx] = arr[pivotIdx], arr[j]
                pivotIdx += 1

        arr[compIdx], arr[pivotIdx] = arr[pivotIdx], arr[compIdx]
        
        return pivotIdx

def quicksort(arr, low, high, rootPt, K):
    if low < high:
        pivot = partition(arr, low, high, rootPt, K)
        if pivot == K-1:
            return
        quicksort(arr, low, pivot-1, rootPt, K)
        quicksort(arr, pivot+1, high, rootPt, K)


def findKNeighbor(P, K, arr):
    rootPt = Point(P[0], P[1])
    ptArr = []
    for pt in arr:
        p = Point(pt[0], pt[1])
        ptArr.append(p)

    print quicksort(ptArr, 0, len(arr)-1, rootPt, K)
    print ptArr

if __name__ == "__main__":
    rootPt = [0,0]
    K = 3
    ptArr = [[-1,-1],[2,4],[5,3],[1,0],[1,2],[1,3],[3,1]]
    findKNeighbor(rootPt, K, ptArr)
    print "---"
    rootPt_class = Point(rootPt[0],rootPt[1])

    for pt in ptArr:
        pt_class = Point(pt[0],pt[1])
        print (pt, rootPt_class-pt_class)