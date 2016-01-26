
def printSnakeString(inputStr):
    N = len(inputStr)
    inputStr = inputStr.replace(" ", "~")
    outStr = ""

    def printFirstLine():
        for i in xrange(2, N, 4):
            if i == 2:
                outStr += "  "
            else:
                outStr += "   "
            outStr += inputStr[i]
        print outStr
    printFirstLine()

    def printSecondLine():
        for i in xrange(1, N, 2):
            outStr += " "
            outStr += inputStr[i]
        print outStr
    printSecondLine()

    def printThirdLine():
        for i in xrange(0, N, 4):
            if i != 0:
                outStr += "   "
            outStr += inputStr[i]
        print outStr
    printThirdLine()

printSnakeString("Hello World Please Work")