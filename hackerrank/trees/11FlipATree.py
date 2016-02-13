class Node(object):
    def __init__(self, val=None, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def flip_a_tree(root):
    if not root:
        return None 
    root.left = flip_a_tree(root.right)
    root.right = flip_a_tree(root.left)
    return root

def print_in_order(root):
    if root.left: print_in_order(root.left)
    print root.val
    if root.right: print_in_order(root.right)

n = Node(val=6,left=Node(val=3,left=Node(val=7),right=Node(val=3)),right=Node(val=4,left=Node(val=8),right=Node(val=1)))

print_in_order(n)

print ""
# 1 4 8 6 3 3 7
filp =flip_a_tree(n)
print_in_order(filp)
