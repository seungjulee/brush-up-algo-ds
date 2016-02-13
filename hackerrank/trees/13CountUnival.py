class Node(object):
    def __init__(self, left=None,right=None,val=None):
        self.left = left
        self.right = right
        self.val = val

def is_unival_tree(root):
    def unival_tree_helper(root, count):
        if not root:
            return True

        left = unival_tree_helper(root.left, count)
        right = unival_tree_helper(root.right, count)

        if left and right:
            if root.left and root.left.val != root.val:
                return False
            if root.right and root.right.val != root.val:
                return False
            count += 1
            return True
        return False
    count = 0
    print unival_tree_helper(root, count)
    return count

n = Node(val=5,
    left=
        Node(val=5, left=Node(val=5, left=Node(val=5)),right=Node(val=5)),
    right=
        Node(val=5,left=Node(val=5),right=Node(val=5))
    )
print is_unival_tree(n)