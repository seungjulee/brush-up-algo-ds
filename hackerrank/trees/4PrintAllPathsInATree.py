import pdb
class Node(object):
    def __init__(self, val=None, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def print_all_paths(root, arr):
    if not root:
        print arr
        return
    arr.append(root.val)
    # pdb.set_trace()
    print_all_paths(root.left, arr)
    # pdb.set_trace()

    if root.right: print_all_paths(root.right, arr) 
    # pdb.set_trace()
    arr.pop()
    
# def makeList(tree):
#     paths = []
#     if not (tree.left or tree.right):
#         return [[tree.val]]
#     if tree.left:
#         paths.extend([[tree.val] + child for child in makeList(tree.left)])
#     if tree.right:
#         paths.extend([[tree.val] + child for child in makeList(tree.right)])
#     return paths

n = Node(val=1,left=Node(val=2, left=Node(val=4),right=Node(val=5)),right=Node(val=3,left=Node(val=6),right=Node(val=7)))

print_all_paths(n,[])
# print makeList(n)