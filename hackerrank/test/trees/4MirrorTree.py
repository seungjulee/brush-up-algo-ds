class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mirror_tree(root):
    if not root:
        return 
    mirror_tree(root.left)
    mirror_tree(root.right)

    root.left, root.right = root.right, root.left

def print_in_order(root):
    if root.left:
        print_in_order(root.left)
    print root.val
    if root.right:
        print_in_order(root.right)

n = Node(2, left=Node(1), right=Node(3, left=Node(2.5), right=Node(4)))

print "BEFORE", print_in_order(n)
mirror_tree(n)
print "AFTER", print_in_order(n)
