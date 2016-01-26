# Complete the function below.
def walkThrough(word, c, board, i, j, visited):
    if c == len(word):
        return True
    elif i < 0 or j < 0:
        return
    elif i >= len(board[0]) or j >= len(board):
        return

    if board[i][j] ==  word[c]:
        visited[i][j] = 1
        walkThrough(word,c+1,board,i-1,j,visited)
        walkThrough(word,c+1,board,i,j-1,visited)
        walkThrough(word,c+1,board,i-1,j-1,visited)
        walkThrough(word,c+1,board,i+1,j,visited)
        walkThrough(word,c+1,board,i,j+1,visited)
        walkThrough(word,c+1,board,i+1,j+1,visited)
    else:
        return False


def wordExists(word, board):
    c = word[0]
    
    startIJ = ()
    visited = [[0 for i in xrange(0,len(board[0]))] for j in xrange(0,len(board))]    
    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if item == c:
                startIJ = (i, j)
                return walkThrough(word, 1, board, i, j, visited)
    return

def findWords(dictionaryList, board):
    N = len(board)

    result = []
    for word in dictionaryList:
        if wordExists(word, board):
            result.append(word)
    return result
    
if __name__ == "__main__":
    dictionaryList = ['GEEK', 'FOR', 'QUIZ', 'GO']
    board = [['G','I','Z'],['U','E','K'],['Q','S','E']]
    print findWords(dictionaryList, board)