def find_best_path(arr, i, j):
    N = len(arr)
    M = len(arr[0])

    if i == N-1 and j == M-1:
        return arr[i][j]
    elif i < N-1 and j == M-1:
        return arr[i][j] + find_best_path(arr, i+1, j)
    elif i == N-1 and j < M-1:
        return arr[i][j] + find_best_path(arr, i, j+1)
    else:
        return arr[i][j] + max(find_best_path(arr, i+1, j), find_best_path(arr, i, j+1))

def find_best_path_dp(arr, i, j):
    memo = [[0 for col in rows] for rows in arr]
    def find_best_path_helper(arr, i, j):
        N = len(arr)
        M = len(arr[0])
        if i == N-1 and j == M-1:
            return memo[i][j]
        elif i < N-1 and j == M-1:
            if memo[i][j] == 0:
                memo[i][j] = arr[i][j] + find_best_path(arr, i+1, j)
            return memo[i][j]
        elif i == N-1 and j < M-1:
            if memo[i][j] == 0:
                memo[i][j] = arr[i][j] + find_best_path(arr, i, j+1)
            return memo[i][j]
        else:
            if memo[i][j] == 0:
                memo[i][j] = arr[i][j] + max(find_best_path(arr, i+1, j), find_best_path(arr, i, j+1))
            return memo[i][j]
    return find_best_path_helper(arr, i, j)



def test_recursion():
    find_best_path(path, 0, 0)
    # for i in range(10):
        
    # for i in range(1):
    #     find_best_path(path, 0, 0)
def test_dp():
    find_best_path_dp(path, 0, 0)
    # for i in range(10):
        

path = [[1,2,5,5,5,5],
        [0,5,6,5,5,5],
        [0,0,1,5,5,5],
        [0,0,1,5,5,5],
        [0,0,1,5,5,5],
        [0,0,1,5,5,5]
        ]
maxnum = 1+2+5+6+1
# print find_best_path(path, 0, 0), maxnum
# print find_best_path_dp(path, 0, 0), maxnum

import timeit
print "recursion", (timeit.timeit("test_recursion()", setup='from bestPath2DMatrix import test_recursion'))
print "dp", (timeit.timeit("test_dp()", setup='from bestPath2DMatrix import test_dp'))
#print (timeit.timeit("test_dp()", setup='from bestPath2DMatrix import test_dp'))

