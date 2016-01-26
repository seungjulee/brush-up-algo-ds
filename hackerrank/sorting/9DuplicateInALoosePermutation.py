def  findDuplicateFromPermutation( intArray):
    N = len(intArray)
    if N == 0 or (N == 1 and N[1] != 1):
        return -1
    bucket = [0 for i in xrange(0,N)]
    has_one = has_N = False

    for val in intArray:
        # check corner cases
        if val > N or val <= 0:
            return -1
        elif val == 1:
            has_one = True
        elif val == N:
            has_N = True

        bucket[val-1] += 1

    if not has_one or not has_N:
        return -1

    for idx, val in enumerate(bucket):
        if val > 1:
            return idx+1

    return -1

if __name__ == "__main__":
    a = [1,7,4,3,2,7,4]
    b = [3,1,2,3]
    c = [5,1,3,5,4,6]
    print findDuplicateFromPermutation(c)