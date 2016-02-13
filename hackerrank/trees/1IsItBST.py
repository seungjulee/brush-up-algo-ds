from sys import maxint
class Node(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_it_bst(node):
    def helper(node, minV, maxV):
        if not node:
            return True

        if minV < node.val < maxV and helper(node.left, minV, node.val) and helper(node.right, node.val, maxV):
            return True
        else:
            return False
    return helper(node, -maxint, maxint)

