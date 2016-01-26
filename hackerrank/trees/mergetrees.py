# Enter your code here. Read input from STDIN. Print output to STDOUT
class Node:
    def __init__(self, left = None, right = None, data = None):
        self.left = left
        self.right = right
        self.data = data

def mergeNodes(n1, n2):
    l1 = convertTreeToList(n1, [])
    l2 = convertTreeToList(n2, [])

    
def DFS(root):
    s = []
    s.append(root)
    while s:
        n = s.pop()
        if n != None:
            


def convertNodeToList(root, l):
    if root == None or root.data == None:
        return

def main():
    t1 = Node(left=Node(data=1), right=Node(data=3), data=2)
    t2 = Node(left=Node(data=6), right=Node(data=8), data=7)

    DFS(t1)


main()