class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)
def count_subtrees_until_k(root, cnt, k=None, arr=None):
    if root.left:
        cnt = count_subtrees_until_k(root.left, cnt, k, arr)[0]
    if arr is not None and cnt >= k:
        arr.append(root)
    cnt += 1
    if root.right:
        cnt = count_subtrees_until_k(root.right, cnt, k, arr)[0]
    return (cnt, arr)

def get_top_K_from_BST(root, K):
    N = count_subtrees_until_k(root, 0)[0]
    if K > N:
        raise "There are only", N, "elements in the tree!"
    N_minus_K = N - K
    top_K_arr = count_subtrees_until_k(root, 0, N-K, [])[1]
    print top_K_arr


n = Node(2, left=Node(1), right=Node(3, left=Node(2.5), right=Node(4)))

print get_top_K_from_BST(n, 4)