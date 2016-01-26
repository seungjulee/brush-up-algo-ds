class Node:
    def __init__(self, left = None, right = None, data = None):
        self.left = left
        self.right = right
        self.data = data

def printAllPaths(root, path):
    if root:
        path.append(root.data)

    if not root.left and not root.right:
        print path
    else:
        printAllPaths(root.left, path)
        printAllPaths(root.right, path) 

#test
t1 = Node(left=Node(data=1), right=Node(data=3), data=2)
printAllPaths(t1, [])