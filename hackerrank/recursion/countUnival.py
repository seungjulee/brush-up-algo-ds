class Node(object):
    def __init__(self, left = None, right = None, val = None):
        self.left = left
        self.right = right
        self.val = val

def count_unival(root):
    if not root:
        return (0, True)

    res = zip(count_unival(root.left), count_unival(root.right))
    summation = sum(res[0])
    is_unival = res[1][0] and res[1][1]

    if is_unival and (not root.left or root.left.val == root.val) and (not root.right or root.right.val == root.val):
        summation += 1
        return (summation, True)

    return (summation, True)


n = Node(Node(Node(val=1),Node(left=Node(val=2), right=Node(val=2), val=2), val=1),Node(val=1), 1)

print count_unival(n)