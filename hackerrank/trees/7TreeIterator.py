class BSTIterator(object):
    def __init__(self, root):
        self.stack = []
        self.buildBST(root)

    def hasNext(self):
        return True if self.stack else False

    def next(self):
        tmp = self.stack.pop()
        self.buildBST(tmp.right)
        return tmp.val

    def buildBST(self, root):
        while root:
            self.stack.append(root)
            root = root.left