class BSTNode(object):
    def __init__(self, left=None,right=None,val=None):
        self.left = left
        self.right = right
        self.val = val

    def __repr__(self):
        return str(self.val)

    def iterative_post_order(self):
        stack = [self]
        prev = None
        while stack:
            curr = stack[-1]
            if (not prev or prev.left is curr or prev.right is curr):
                if curr.left:
                    stack.append(curr.left)
                elif curr.right:
                    stack.append(curr.right)
                else:
                    print curr.val
                    stack.pop()
            elif curr.left is prev:
                if curr.right:
                    stack.append(curr.right)
                else:
                    print curr.val
                    stack.pop()
            elif curr.right is prev:
                print curr.val
                stack.pop()
            prev = curr



