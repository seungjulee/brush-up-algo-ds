class Node(object):
    def __init__(self):
        self.children = []
        self.val = 0
    def getDiameter(self):
        highestPath = 0
        if not self.children:
            return highestPath
        while self.children:
            for child in children:
                if child.children:


