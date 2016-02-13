class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def balanced_bst_from_sorted_arr(arr, start, end):
    if start > end:
        return None

    mid = (start+end) // 2
    root = Node(arr[mid])
    root.left = balanced_bst_from_sorted_arr(arr, start, mid-1)
    root.right = balanced_bst_from_sorted_arr(arr, mid+1, end)
    return root

def print_line_by_line(root):

    if not root:
        return

    thisline = [root]
    while thisline:
        nextline = []
        for root in thisline:
            print root.val,
            if root.left:
                nextline.append(root.left)
            if root.right:
                nextline.append(root.right)
        print
        thisline=nextline

a = [8,10,12,15,16,20,15]
node = balanced_bst_from_sorted_arr(a, 0, len(a)-1)
print_line_by_line(node)