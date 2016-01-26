def moveStack(N, source, spare, dest):
    if N > 0:
        moveStack(N-1, source, dest, spare)
        print (source, spare, dest)
        if source != []:
            dest.append(source.pop())
        moveStack(N-1, spare, source, dest)
        print (source, spare, dest)

    
def playTowerOfHanoi():
    N = 5
    A = list(reversed(range(1,N+1)))
    B = []
    C = []

    moveStack(N, A, B, C)

playTowerOfHanoi()