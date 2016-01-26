from collections import defaultdict
def checkPalindrome(word):
    c = [0] * 256
    for s in word:
        c[ord(s)] += 1

    if len(word) % 2 == 0:
        isEven = True
    else:
        isEven = False

    hasOdd = False

    for s in word:
        if isEven:
            if c[ord(s)] % 2 == 1:
                return False
        else:
            if not hasOdd and c[ord(s)] % 2 == 1:
                hasOdd = True
            elif hasOdd and c[ord(s)] % 2 == 1:
                return False

    return True

def main(s):
    print checkPalindrome(s)

msg = raw_input()
main(msg)