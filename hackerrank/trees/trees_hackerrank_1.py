class TreeNode:
    def __init__(self, left = None, right = None):
        self.left = left
        self.right = right

def walkThroughTress(nCount, possibleTrees, node):
	if nCount == 1:
		possibleTrees += 1
		return
	else:
		
		walkThroughTress(nCount, possibleTrees)


def countTrees(iNodeCount):
    N = iNodeCount


    print N


countTrees(1)
