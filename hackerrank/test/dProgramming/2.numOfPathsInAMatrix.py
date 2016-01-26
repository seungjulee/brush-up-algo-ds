def findTotalPath(a, startX, startY, endX, endY, res):
    if startX == endX and startY == endY:
        res.append(1)
        return
    if startX > endX or startY > endY:
        return

    if a[startY][startX] == 0:
        return

    findTotalPath(a, startX+1, startY, endX, endY, res)
    findTotalPath(a, startX, startY+1, endX, endY, res)
    
    
def numberOfPaths (a):
    res = []
    endX = len(a[0])-1
    endY = len(a)-1
    findTotalPath(a, 0, 0, endX, endY, res)
    
    return sum(res)

if __name__ == "__main__":
    a = [[1,1,1,1],[1,1,1,1],[1,1,1,1]]
    b = [[1,1],[0,1]]
    print numberOfPaths(a)
