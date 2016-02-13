def popcount(v):
    v = v - ((v>>1) & 0x55555555);
    v = (v & 0x33333333) + ((v>>2) & 0x33333333);
    return ((v + (v>>4) & 0xF0F0F0F) * 0x1010101) >> 24;
def get_hamming_weight(arr):
    # cnt = 0
    # for num in arr:
    #     cnt += bin(num).count("1")
    # return cnt
    c = 0
    for item in arr:
        while item:
            item &= item - 1
            c += 1
     
        return c 

    # 4 byte == 32 bit
    # bin(num).count("1")
    # bit_counter = {x:y for bin_num in }
    # cnt = 0
    # n = 32
    # for item in arr:
    #     while item is not 0:
    #         if item > 2**n:
    #             item -= 2**(n+1)
    #             n -= 1
    #             cnt += 1
    #         else:
    #             n -= 1

print popcount(31)+popcount(51), "expected 9"
print get_hamming_weight([2147483647,3]), "expected 33"