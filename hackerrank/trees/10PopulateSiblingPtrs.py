class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.nextRight = None

# class SibilingNode(object):
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.sibiling = None


def populate_sibiling_ptr(root):
    if not root
        return
    if root.left:
        root.left.nextRight = root.right
    if root.right:
        root.right.nextRight = root.nextRight.left if root.nextRight else None

    populate_sibiling_ptr(root.left)
    populate_sibiling_ptr(root.right)