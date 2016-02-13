def fibonacci():
    memo = [0,1]
    while True:
        yield memo[0]
        memo[0], memo[1] = memo[1], memo[0]+memo[1]

for n in fibonacci():
    if n < 100:
        print n
            
