from math import sqrt 
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __repr__(self):
        return "(%s, %s)" % (self.x, self.y)

class KMinHeap(object):
    def __init__(self, K, rootPt):
        self.heapList = [0]
        self.heapSize = 0
        self.KMin = K
        self.rootPt = rootPt

    def percUp(self, i):
        while i // 2 > 0:
            if self.rootPt - self.heapList[i] > self.rootPt - self.heapList[i // 2]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[i // 2]
                self.heapList[i // 2] = tmp
            i = i // 2

    def percDown(self, i):
        while i*2 <= self.heapSize:
            minChildIdx = self.getminChildIdx(i)
            if self.rootPt - self.heapList[minChildIdx] > self.rootPt - self.heapList[i]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[minChildIdx]
                self.heapList[minChildIdx] = tmp
            i = minChildIdx

    def delMin(self):
        deleted = self.heapList[1]
        self.heapList[1] = self.heapList[self.heapSize]
        self.heapSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return deleted

    def buildHeap(self, arr):
        self.heapSize = len(arr)
        self.heapList = [0] + arr[:]
        i = len(arr) // 2
        while i > 0:
            self.percDown(i)
            i -= 1

    def getminChildIdx(self, i):
        if i*2+1 > self.heapSize:
            return i*2
        elif self.rootPt - self.heapList[i*2] > self.rootPt - self.heapList[i*2+1]:
            return i*2
        else:
            return i*2+1

    def insert(self, item):
        if self.heapSize < self.KMin:
            self.heapList.append(item)
            self.heapSize += 1
            self.percUp(self.heapSize)
        elif self.rootPt - item < self.rootPt - self.heapList[1]:
            self.delMin()
            self.insert(item)

    def printKMaxItem(self):
        deletedArr = []
        while self.heapSize > 0:
            deleted = self.delMin()
            print deleted, self.rootPt - deleted
            deletedArr.append(deleted)

        self.buildHeap(deletedArr)

def findKNeighbor(P, K, ptArr):
    rootPt = Point(P[0], P[1])
    KHeap = KMinHeap(K, rootPt)
    for pt in ptArr:
        p = Point(pt[0], pt[1])
        KHeap.insert(p)
    KHeap.printKMaxItem()

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
