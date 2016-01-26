# Enter your code here. Read input from STDIN. Print output to STDOUT
def printWildcard(string, wildcardList, i, N):
    if i == N:
        wildcardList.append(string)
        return wildcardList
    elif string[i] == "?":
        zeroString = "".join(string[:i-1]+"0"+string[i:])
        
        wildcardList = printWildcard(zeroString, wildcardList, i+1, N)
        
        oneString = "".join(string[:i-1]+"1"+string[i:])
        wildcardList = printWildcard(oneString, wildcardList, i+1, N)
        
        return wildcardList
    else:
        wildcardList = printWildcard(string, wildcardList, i+1, N)
        return wildcardList

def main():
    wildcard = "1?1?"
    N = len(wildcard)
    wildcardList = []
    wildcardList = printWildcard(wildcard, wildcardList, 0, N)
    print wildcardList

main()