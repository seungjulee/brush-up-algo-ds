class BST(object):
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
    def __eq__(self, other):
        if not self or not other:
            return False
        if self.val is not other.val:
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
        if not self:
            return
        if not self.val:
            self.val = val
            return

        if val < self.val:
            if not self.left:
                self.left = BST(val)
            else:
                self.left.insert(val)
        else:
            if not self.right:
                self.right = BST(val)
            else:
                self.right.insert(val)

    def search(self, val, parent=None):
        if val == self.val:
            return (True, self, parent)
        elif val < self.val:
            if not self.left:
                return (False, None, None)
            else:
                return self.left.search(val, self)
        else:
            if not self.right:
                return (False, None, None)
            else:
                return self.right.search(val, self)

    def count_children(self):
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt
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

    def delete(self, val):
        exist, found, found_parent = self.search(val)
        num_child = self.count_children()
        from_left = (found_parent.left == found if found_parent else None)
        if not exist:
            raise ("key", val, "is not available!")

        if num_child == 0:
            if found_parent:
                if from_left:
                    found_parent.left = None
                else:
                    found_parent.right = None
                del found
            else:
                # at the root
                self.val = None
        elif num_child == 1:
            child = found.left or found.right
            if found_parent:
                if from_left:
                    found_parent.left = child
                else:
                    found_parent.right = child
                del found
            else:
                self.val = child.val
                self.left = child.left
                self.right = child.right
        else:
            parent = found
            successor = found.right
            while successor.left:
                parent = successor
                successor = successor.left
            found.val = successor.val
            if parent.left == successor:
                parent.left = successor.right
            else:
                parent.right = successor.right






    def print_in_order(self):
        if not self:
            return
        if self.left:
            self.left.print_in_order()
        print self.val
        if self.right:
            self.right.print_in_order()

def test_BST():
    def insert_arr(arr, bst):
        for i in arr:
            bst.insert(i)
        return bst

    def test_search(bst, val):
        return bst.search(val)[0]
    
    def test_main():
        arr = [8,3,10,1,6,4,7,14,13]
        bst = insert_arr(arr, BST())
        #bst.print_in_order()
        print test_search(bst, 1), "expected True"
        print test_search(bst, 19), "expected False"

    test_main()




if __name__ == "__main__":
    test_BST()