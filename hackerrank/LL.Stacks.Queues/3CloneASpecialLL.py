class Node:
    def __init__(self, val, first=None, second=None):
        self.val = val
        self.first = first
        self.second = second


def clone_a_special_list(root):
    node = Node(root.val)
    while root.first:
        node.val = root.val
        node.first = root.first
        root = root.first
