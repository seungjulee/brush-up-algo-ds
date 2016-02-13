# 1. build123
# 2. size
# 3. maxDepth
# 4. minValue
# 5. printTree (inorder)
# 6. printPostorder (dfs)
# 7. hasPathSum
#
class Node(object):
    def __init__(self, val=None, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        print self.left.val, self.val, self.right.val

def insert(root, val):
    if not root:
        return Node(val=val)
    else:
        if val <= root.val: 
            root.left = insert(root.left, val)
        else:
            root.right = insert(root.right, val)
        return root


def build123_a():
    return Node(val=2, left=Node(val=1), right=Node(val=3))


def build123_c():
    n = Node()
    n = insert(n,1)
    n = insert(n,2)
    n = insert(n,3)
    return n

print build123_c()
