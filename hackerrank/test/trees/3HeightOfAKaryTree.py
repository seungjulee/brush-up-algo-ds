class KaryNode:
    def __init__(self, val, children=None):
        self.val = val
        self.children = children
    
# def DFS(root):
#     stack = [root]
#     max_cnt = 0
#     curr_cnt = 0
#     while stack:
#         node = stack.pop()
#         curr_cnt += 1
#         if not node.children and max_cnt < curr_cnt:
#             max_cnt = curr_cnt

#         for child in list(reversed(node.children)):
#             stack.append(child)

#     return max_cnt

def max_depth(root):
    if not root:
        return 0

    children_cnt = []

    for child in root.children:
        children_cnt.append(child)

    # left_cnt = max_depth(root.left)
    # right_cnt = max_depth(root.right)

    max_depth = max(children_cnt) + 1
    return max_depth
