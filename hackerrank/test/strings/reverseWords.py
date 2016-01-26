def reverseStr(s):
    newStr = s[::-1]

    return ' '.join(w[::-1] for w in newStr.split())


def main():
    print reverseStr("I will do it.")

main()