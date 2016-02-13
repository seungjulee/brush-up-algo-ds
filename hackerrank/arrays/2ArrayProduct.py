# Input : [1, 2, 3, 4, 5]
# Output: [(2*3*4*5), (1*3*4*5), (1*2*4*5), (1*2*3*5), (1*2*3*4)]
#       = [120, 60, 40, 30, 24]

# def reduce_wo_item(arr):
#     for i, v in enumerate(arr):
#         if not arr[:i]:
#             yield reduce(lambda x, y: x*y, arr[i+1:])
#         elif not arr[i+1:]:
#             yield reduce(lambda x, y: x*y, arr[:i])
#         else:
#             yield reduce(lambda x, y: x*y, arr[:i]) * reduce(lambda x, y: x*y, arr[i+1:])

# def get_array_product(arr):
#     res = []
#     for item in reduce_wo_item(arr):
#         res.append(item)

#     return res


def get_array_product(arr):
    left_prod_arr = []
    right_prod_arr = []
    comb_prod_arr = []
    N = len(arr)
    left_prod = 1
    right_prod = 1

    for i in xrange(0, N):
        left_prod_arr.append(left_prod)
        left_prod = left_prod * arr[i]

    for i in reversed(xrange(0,N)):
        right_prod_arr.append(right_prod)
        right_prod = right_prod * arr[i]

    print left_prod_arr, right_prod_arr

    for i in xrange(0, N):
        comb_prod_arr.append(left_prod_arr[i]*right_prod_arr[(N-1)-i])

    return comb_prod_arr   


print get_array_product([1,2,3,4,5])
