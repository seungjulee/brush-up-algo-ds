def  sortCharacters( inString):
    chrArr = [0] * 256
    for c in inString:
        chrArr[ord(c)] += 1

    inString = ""
    for i,freq in enumerate(chrArr):
        if freq > 0:
            while freq > 0:
                inString += chr(i)
                freq -= 1
    return inString

def main():
    t1 = "This is easy"
    t1_expected = "  Taehiisssy"
    t2 = "The quick brown fox jumps over the lazy dog"
    t2_expected = "        Tabcdeeefghhijklmnoooopqrrstuuvwxyz"
    sortCharacters(t1)
    assert sortCharacters(t2) == t2_expected, "t1 error"

main()