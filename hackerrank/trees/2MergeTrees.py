from collections import deque
def merge_two_arrays(self_arr, other_arr):
    sorted_arr = []
    while self_arr and other_arr:
        if self_arr[0] < other_arr[0]:
            sorted_arr.append(self_arr.pop(0))
        else:
            sorted_arr.append(other_arr.pop(0))
    either = self_arr or other_arr
    while either:
        sorted_arr.append(either.pop(0))
    return sorted_arr
def build_bst_from_sorted_arr(arr,start,end):
    if start > end:
        return None
    mid = (start+end )//2
    root = BSTNode(val=arr[mid])
    root.left = build_bst_from_sorted_arr(arr, start,mid-1)
    root.right = build_bst_from_sorted_arr(arr, mid+1,end)
    return root

class BSTNode(object):
    def __init__(self, left=None,right=None,val=None):
        self.left = left
        self.right = right
        self.val = val

    def __repr__(self):
        return str(self.val)

    def __add__(self, other):
        self_arr = [item for item in self.in_order_generator()]
        other_arr = [item for item in other.in_order_generator()]
        sorted_arr = merge_two_arrays(self_arr, other_arr)
        return build_bst_from_sorted_arr(sorted_arr,0,len(sorted_arr)-1)
        
    
    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            print "Duplicate element already in the tree skipped!"
            return

        if val < self.val:
            if not self.left:
                self.left = BSTNode(val=val)
            else:
                self.left.insert(val)
        else:
            if not self.right:
                self.right = BSTNode(val=val)
            else:
                self.right.insert(val)
    def search(self, val, parent=None):
        if not self.val:
            return (False, None, None)

        if self.val == val:
            return (True, self, parent)


        if val < self.val:
            if self.left:
                self.left.search(val)
            else:
                return (False, None, None)
        else:
            if self.right:
                self.right.search(val)
            else:
                return (False, None, None)
    def get_how_many_children(self):
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt

    def delete(self, val):
        exist, found_node, parent_node = self.search(val)
        if not exist:
            raise "Key does not exist in the tree!"

        num_child = found_node.get_how_many_children()
        from_left = found_node == parent_node.left if parent_node else None
        if num_child == 0:
            if parent_node:
                if from_left:
                    parent_node.left = None
                else:
                    parent_node.right = None
                del found_node
            else:
                self.val = None
        elif num_child == 1:
            child = found_node.left or found_node.right
            if parent_node:
                if from_left:
                    parent_node.left = child
                else:
                    parent_node.right = child
                del found_node
            else:
                found_node.val = child.val 
                found_node.left = child.left
                found_node.right = child.right
        else:
            parent = found_node
            successor = parent.right
            while successor.left:
                parent = successor
                successor = successor.left
            parent.val = successor.val
            if parent.left == successor:
                parent.left = successor.right
            else:
                parent.right = successor.right

    def in_order_generator(self):
        if self.left:
            for val in self.left.in_order_generator():
                yield val
        yield self.val
        if self.right:
            for val in self.right.in_order_generator():
                yield val

    def print_in_order(self):
        if self.left:
            self.left.print_in_order()
        print self.val
        if self.right:
            self.right.print_in_order()

    def DFS(self):
        if not self.val:
            return

        stack = [self]
        while stack:
            node = stack.pop()
            print node
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            
    def BFS(self):
        if not self.val:
            return
        q = deque()
        q.append(self)
        while q:
            node = q.popleft()
            print node
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def print_tree_by_line(self):
        thisline = [self]
        while thisline:
            nextline = []
            for n in thisline:
                print n,
                if n.left: nextline.append(n.left)
                if n.right: nextline.append(n.right)
            print
            thisline = nextline

    def print_post_order(self):
        if self.left:
            self.left.print_post_order()
        if self.right:
            self.right.print_post_order()
        print self.val
    
    

n1 = BSTNode(val=2, left=BSTNode(val=1), right=BSTNode(val=3))
n2 = BSTNode(val=7, left=BSTNode(val=6), right=BSTNode(val=8))
n3 = n1+n2

# n3.DFS()
# print "-"
# n3.print_post_order()