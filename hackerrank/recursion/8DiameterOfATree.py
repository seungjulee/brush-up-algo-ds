class Node(object):
    def __init__(self, left = None, right = None, val = None):
        self.left = left
        self.right = right
        self.val = val

def height(root):
    if root == None:
        return 0

    return 1 + max(height(root.left) + height(root.right))

def count_diameter_of_a_tree(root):
    left_dia = 0
    right_dia = 0

    left_height = height(root.left)
    right_height = height(root.right)

    left_dia = 1 + count_diameter_of_a_tree(root.left)
    right_dia = 1 + count_diameter_of_a_tree(root.right)
    both = left_dia + right_dia + 1

    return max(max(left_dia, right_dia), both)



def main():
    Node n1 = Node(left=Node(), right=Node())
