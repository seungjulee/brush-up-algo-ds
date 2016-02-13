class Node(object):
    def __init__(self, val=None, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def clone_tree(orig):
    if not orig:
        return None
    root = Node()
    root.val = orig.val
    root.left = clone_tree(orig.left)
    root.right = clone_tree(orig.right)
    return root

def print_in_order(root):
    if root.left:
        print_in_order(root.left)
    print root.val
    if root.right: print_in_order(root.right)

n = Node(val=1,left=Node(val=2, left=Node(val=4),right=Node(val=5)),right=Node(val=3,left=Node(val=6),right=Node(val=7)))
print_in_order(n)
copied = clone_tree(n)
print "--"
print_in_order(copied)
