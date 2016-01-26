def  printTriplets( intArr):
    def two_sum(arr, target):
        hashmap = {}
        for i, v in enumerate(arr):
            if v in hashmap:
                firstValueIdx = hashmap[v]
                yield arr[firstValueIdx], v
            else:
                hashmap[target - v] = i
    def three_sum(intArr):
        for i, num in enumerate(intArr): 
            for two_nums in two_sum(intArr[i+1:], -num):
                yield (num, two_nums[0], two_nums[1])

    format_res = []
    for res in three_sum(intArr):
        format_res.append("%s,%s,%s" % res)
    
    return format_res