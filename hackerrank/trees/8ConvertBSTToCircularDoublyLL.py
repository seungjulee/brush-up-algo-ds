

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def in_order_generator(self):
        if self.left:
            for val in self.left.in_order_generator():
                yield val
        yield self.val
        if self.right:
            for val in self.right.in_order_generator():
                yield val

def convert_bst_doubly_LL(root):
    cnt = 0
    prev_LL = None
    for val in root.in_order_generator():
        if cnt == 0:
            prev_LL = Node(val)
            first_node = prev_LL
        else:
            curr_LL = Node(val)
            curr_LL.left = prev_LL
            prev_LL.right = curr_LL
            prev_LL = curr_LL
        cnt += 1
    last_node = curr_LL
    last_node.right = first_node
    first_node.left = last_node

    return first_node

def traverse_LL(root):
    while root.left:
        print root.val
        root = root.left

def main():
    n1 = Node(val=2, left=Node(val=1), right=Node(val=3))
    converted_ll = convert_bst_doubly_LL(n1)
    traverse_LL(converted_ll)

main()