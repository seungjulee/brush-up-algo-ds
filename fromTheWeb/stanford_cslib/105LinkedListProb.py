class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        root = self
        while root.next:
            print root.val,
            root = root.next
        print
    
    def count(self):
        root = self
        cnt = 0
        while root.next:
            cnt += 1
            root = root.next
        return cnt
    def getNth(self,n):
        root = self
        cnt = 0
        while cnt < n:
            root = root.next
            cnt += 1
            if not root:
                raise "There are less than N objects"
        return root
    def delList(self):
        self.val = None
        self.next = None
    def pop(self):
        tmp = Node(self.val)
        self.next = self.next.next
        self.val = self.next.val
        return tmp
    def insertNth(self, n, node):
        cnt = 0
        root = self
        while cnt < n-1:
            root = root.next

        node.next = root.next.next
        root.next = node
        return
    def sortedInsert(self, node):
        root = self
        while root.next.val > node.val:
            root = root.next

        node.next = root.next
        root.next = node
    def insertSort(self):
        s


a = Node()

