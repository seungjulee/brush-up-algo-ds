class Node(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def find_LCA(self, val1, val2):
        if not self.val:
            return None

        if self.val is (val1 or val2):
            return self

        left = self.left.find_LCA(val1, val2)
        right = self.right.find_LCA(val1, val2)

        if left and right:
            return self
        else:
            return left or right