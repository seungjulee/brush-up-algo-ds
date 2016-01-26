# import copy

# def solveNQueens(grid, x, y):
#     N = len(grid[0])

#     if N != len(grid):
#         raise "Not in a same dimension"

#     if x >= N:
#         solveNQueens(grid, 0, y+1)

#     if x == N-1 and y == N-1:
#         return grid

#     if grid[y][x] == 0:
#         solveNQueens(grid, x+1, y)
#         solveNQueens(grid, x, y+1)

# def checkBoundary(grid, x, y):
#     N = len(grid[0])

    
# def main():
#     N = 4
#     grid = [ [ 0 for col in xrange(N)] for row in xrange(N)]
#     print solveNQueens(grid, 0, 0)

# def printGrid():
#     pass

# if __name__ == "__main__":
#     main()

def solveNQueens( n):
    def DFS(queens, xy_dif, xy_sum):
        p = len(queens)
        if p==n:
            result.append(queens)
            return None
        for q in range(n):
            print p, q, queens, xy_dif, xy_sum
            if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                
                DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
    result = []
    DFS([],[],[])
    return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]

for line in solveNQueens(4):
    for l in line:
        print l
    print 