def get_sum_zero_items(arr, target=0):
    def two_sum(arr, target):
        hashmap = {}
        for i,v in enumerate(arr):
            if v in hashmap:
                first_idx = hashmap[v]
                yield arr[first_idx], arr[i]
            else:
                hashmap[target-v] = i
    def three_sum(arr):
        isZero = False
        for i,v in enumerate(arr):
            if v == 0:
                isZero = True
                yield 0
            for first_val, second_val in two_sum(arr[i+1:], -v):
                if isZero:
                    yield v, first_val, second_val
                    yield 0, v, first_val, second_val
    return list(three_sum(arr))



get_sum_zero_items([5,1,2,-3,7,-4])