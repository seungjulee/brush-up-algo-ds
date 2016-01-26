import copy

def isPalindrome(s):
    left = 0
    right = len(s)-1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

def addPalindrome(s, start, partition, res):
    if len(s) == start:
        # temp = copy.deepcopy(partition)
        temp = list(partition)
        res.append(temp)

        return

    for i in xrange(start+1, len(s)+1):
        subString = s[start:i]
        if isPalindrome(subString):
            partition.append(subString)
            addPalindrome(s, i, partition, res)
            partition.pop()

def main():
    s = "abracadabra"
    start = 0
    partition = []
    res = []

    addPalindrome(s, start, partition, res)

    for i in res:
        line = ""
        for j in i:
            line += j + "|" 
        print line



if __name__ == "__main__":
    main()