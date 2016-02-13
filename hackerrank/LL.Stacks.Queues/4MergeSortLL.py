class LinkedListNode:
    def __init__(self, node_value):
        self.val = node_value
        self.next = None

def merge_sort(root):
    def merge_sort_helper(arr, low, high):
        if low < high:
            mid = (low+high) // 2
            merge_sort_helper(arr, low, mid)
            merge_sort_helper(arr, mid+1, high)
            merge(arr, low, mid, high)


    