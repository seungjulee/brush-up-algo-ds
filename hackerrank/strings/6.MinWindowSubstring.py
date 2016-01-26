# https://leetcode.com/discuss/72701/here-10-line-template-that-can-solve-most-substring-problems?show=72701#q72701
# https://leetcode.com/discuss/5469/is-the-length-of-t-considered-constant-or-m
from collections import defaultdict
def findMinWindowSubstring(S, T):
    """

    """
    required = [0] * 256; minLen= 1242145234

    for c in T:
        required[ord(c)] += 1
    
    start, end = 0, 0
    minStart, minEnd = 0,0
    count = len(T)

    for i in xrange(len(S)):
        required[ord(S[i])] -= 1
        if required[ord(S[i])] == 0:
            if count != 1:
                count -= 1
            else:
                for j in xrange(start,i+1):
                    required[ord(S[j])] += 1
                    # find the first elm
                    if required[ord(S[j])] > 0:
                        length = i-j
                        if length < minLen:
                            minLen = length
                            minStart, minEnd = j, i
                        start = j+1
                        break
    if count == 1:
        return S[minStart: minEnd+1]
    else:
        return ""



def main():
    S = "ADOBECODEBANC" #"AYZABOBECODXBANC"
    T = "ZYD"  #"ABC"
    print findMinWindowSubstring(S, T)

main()
