class BinaryHeap(object):
    def __init__(self, arr=None):
        # heapList[0] is always 0. The list starts from 1
        if arr:
            self.buildHeap(arr)
        else:
            self.heapList = [0]
            self.currSize = 0


    def percUp(self,i):
        while i // 2 > 0:
            # change to > for max heap
            if self.heapList[i] < self.heapList[i//2]:
                temp = self.heapList[i]
                # move parent to child
                self.heapList[i] = self.heapList[i//2]
                self.heapList[i//2] = temp
            i = i // 2

    def percDown(self,i):
        while i*2 < self.currSize:
            minChildIdx = self.minChild(i)
            if self.heapList[minChildIdx] < self.heapList[i]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[minChildIdx]
                self.heapList[minChildIdx] = temp
            i = minChildIdx

    def delMin(self):
        deleted = self.heapList[1]
        self.heapList[1] = self.heapList[self.currSize]
        self.currSize = self.currSize - 1
        self.heapList.pop()
        self.percDown(1)
        return deleted

    def buildHeap(self, arr):
        i = len(arr) // 2
        self.currSize = len(arr)
        self.heapList = [0] + arr[:]
        while i > 0:
            self.percDown(i)
            i -= 1

    def minChild(self,i):
        if i*2 + 1 > self.currSize:
            return i*2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else
                return i*2+1

    def insert(self, item):
        self.heapList.append(item)
        self.currSize += 1
        self.percUp(self.currSize)



