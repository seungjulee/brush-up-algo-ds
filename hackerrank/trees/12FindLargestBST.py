from sys import maxint
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_largest_bst(root):
    if not root:
        return

    if root.left:
        left_is_bst = is_it_bst(root.left)
    if root.right:
        right_is_bst = is_it_bst(root.right)

    max_node = None
    
    if left_is_bst:
        l_largest = get_largest_node_bst(root.left)
    if right_is_bst:
        r_largest = get_largest_node_bst(root.right)

    if l_largest.val < r_largest.val:
        max_node = r_largest
    else:
        max_node = l_largest
    return max_node


def get_largest_node_bst(root):
    if not root.right:
        return root
    while root.right:
        root = root.right
    return root

def is_it_bst(node):
    def helper(node, minV, maxV):
        if not node:
            return True

        if minV < node.val < maxV and helper(node.left, minV, node.val) and helper(node.right, node.val, maxV):
            return True
        else:
            return False
    return helper(node, -maxint, maxint)


