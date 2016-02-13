# Problem Solving with Algorithms and Data Structure - Binary Heap
# http://interactivepython.org/runestone/static/pythonds/Trees/BinaryHeapImplementation.html
# http://www.eecs.wsu.edu/~ananth/CptS223/Lectures/heaps.pdf

class MinHeap(object):
    def __init__(self):
        self.heapList = [0]
        self.heapSize = 0

    def insert(self, item):
        self.heapList.append(item)
        self.heapSize += 1
        self.percUp(self.heapSize)

    def percUp(self, i):
        while i // 2 > 0: # parent
            if self.heapList[i] < self.heapList[i//2]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[i//2]
                self.heapList[i//2] = tmp
            i = i // 2

    def minChild(self, i):
        if i*2 + 1 > self.heapSize:
            return i*2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1

    def percDown(self, i):
        while i*2 <= self.heapSize:
            minChildIdx = self.minChild(i)
            if self.heapList[minChildIdx] < self.heapList[i]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[minChildIdx]
                self.heapList[minChildIdx] = tmp
            i = minChildIdx

    def buildHeap(self, arr):
        self.heapList = [0] + arr[:]
        self.heapSize += 1
        i = len(arr) // 2

        while i > 0:
            self.percDown(i)
            i -= 1

    def delMin(self):
        deleted = self.heapList[1]
        self.heapList[1] = self.heapList[self.heapSize]
        self.heapSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return deleted

    def printAll(self):
        while self.heapSize > 0:
            print self.delMin()


def mergeSortedArrays(arr):
    K = len(arr)
    N = len(arr[0])
    heap = MinHeap()

    i = 0
    for i in xrange(0, N):
        for k in xrange(0, K):
            #print arr[k][i]
            heap.insert(arr[k][i])
    print ""
    heap.printAll()

if __name__ == "__main__":
    mergeSortedArrays([[1,3,5,7],[2,4,6,8],[0,-1,9,10]])