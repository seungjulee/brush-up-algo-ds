class MinHeap(object):
    def __init__(self, K):
        self.heapList = [0]
        self.heapSize = 0
        self.KMin = K

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[i // 2]
                self.heapList[i // 2] = tmp
            i = i // 2

    def percDown(self, i):
        while i*2 <= self.heapSize:
            minChildIdx = self.getminChildIdx(i)
            if self.heapList[minChildIdx] < self.heapList[i]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[minChildIdx]
                self.heapList[minChildIdx] = tmp
            i = minChildIdx

    def printMin(self):
        arr = []
        while self.heapSize > 0:
            deleted = self.delMin()
            arr.append(deleted)
            print deleted
        self.buildHeap(arr)

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
        elif self.heapList[i*2] < self.heapList[i*2+1]:
            return i*2
        else:
            return i*2+1

    def insert(self, item):
        if self.heapSize < self.KMin:
            self.heapList.append(item)
            self.heapSize += 1
            self.percUp(self.heapSize)
        elif self.heapList[1] < item:
            self.delMin()
            self.insert(item)

if __name__ == "__main__":
    K = 3
    KHeap = MinHeap(K)
    arr = [7,1,23,12,9,30,2,50,2]
    for i in arr:
        KHeap.insert(i)

    KHeap.printMin()
