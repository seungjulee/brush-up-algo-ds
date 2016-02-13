# class Node(object):
#     def __init__(self, data=None, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right
from Queue import Queue 


class BST(object):
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.data)
    def __eq__(self,other):
        if not other:
            return False
        if self.data is not other.data:
            return False

        res = True
        if self.left:
            if not other.left:
                return False
            else:
                res = self.left == other.left

        if not res:
            return False

        if self.right:
            if not other.right:
                return False
            else:
                res = self.right == other.right

        return res

    def insert(self, val):
        if self.data:
            if val < self.data:
                if not self.left:
                    self.left = BST(val)
                else:
                    self.left.insert(val)
            else:
                if not self.right:
                    self.right = BST(val)
                else:
                    self.right.insert(val)
        else:
            self.data = val
    def pre_order_print(self):
        if not self.data:
            return

        print self.data
        if self.left:
            self.left.pre_order_print()
        if self.right:
            self.right.pre_order_print()
    def post_order_print(self):
        if not self.data:
            return

        
        if self.left:
            self.left.post_order_print()
        if self.right:
            self.right.post_order_print()
        print self.data       
    def in_order_print(self):
        if not self.data:
            return

        if self.left:
            self.left.in_order_print()
        print self.data
        if self.right:
            self.right.in_order_print()

    def search(self, val, parent=None):
        if val == self.data:
            return (True, self, parent)
        elif val < self.data:
            if not self.left:
                return (False, None, None)
            return self.left.search(val, self)
        else:
            if not self.right:
                return (False, None, None)
            return self.right.search(val, self)
    def count_children(self):
        cnt = 0 
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt
    def get_children(self):
        if self.count_children() == 0:
            return None
        elif self.count_children() == 2:
            return (self.left, self.right)
        else:
            either = self.left or self.right
            return (either)

    def delete(self, val):
        val_exist, val_node, val_parent = self.search(val)
        # if the node doesn't have children == leaf
        children_cnt = val_node.count_children()
        from_left = ((val_parent.left is val_node) if val_parent else None)
        if children_cnt == 0:
            if val_parent:
                if from_left:
                    val_parent.left = None
                else:
                    val_parent.right = None
                del val_node
            else:
                self.data = None
            return 
        elif children_cnt == 1:
            child = val_node.get_children()
            if val_parent:
                if from_left:
                    val_parent.left = child
                else:
                    val_parent.right = child
                del val_node
            else:
                self.left = child.left
                self.right = child.right
                self.data = child.data
        else:
            parent = val_node
            successor = val_node.right
            while successor.left:
                parent = successor
                successor = successor.left
            val_node.data = successor.data
            if parent.left == successor:
                parent.left = successor.right
            else:
                parent.right = successor.right

    def DFS(self):
        if not self:
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
        if not self:
            return
        q = Queue()
        q.put(self)
        while not q.empty():
            node = q.get()
            print node
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)



def test():
    arr = [11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31]
    arr2 = [8,3,10,1,6,4,7,14,13]
    arr3_1 = [1,3,2]
    arr3_2 = [1,3,11]
   
    # b.in_order_print()
    def test_search(): 
        for i in arr:
            print b.search(i)

    def test_in_order_print(b):
        print "PRINTING INORDER"
        b.in_order_print()
        print ""
    def test3():
        b1 = BST()
        b2 = BST()
        for i in arr3_1:
            b1.insert(i)
        for i in arr3_2:
            b2.insert(i)

        test_in_order_print(b1)
        test_in_order_print(b2)
        print b1 == b2

    def test_dfs():
        b = BST()
        for i in arr:
            b.insert(i)
        test_in_order_print(b)
        b.DFS()

    def test_bfs():
        b = BST()
        for i in arr:
            b.insert(i)
        b.BFS()
    test_bfs()
    # test_dfs()



test()
