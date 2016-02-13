# input {2, 3, -4, -9, -1, -7, 1, -5, -6} 
# output {2, -4, 3, -9, 1, -1, -7, -5, -6}. 

def get_alternative_arr(arr):
    pos_arr = []
    neg_arr = []
    for v in arr:
        if v > 0:
            pos_arr.append(v)
        else:
            neg_arr.append(v)

    pos_term = True
    del arr[:]

    while neg_arr and pos_arr:
        if pos_term:
            arr.append(pos_arr.pop(0))
            pos_term = False
        else:
            arr.append(neg_arr.pop(0))
            pos_term = True

    either_half = neg_arr or pos_arr

    while either_half:
        arr.append(either_half.pop(0))
    return arr


print get_alternative_arr([2, 3, -4, -9, -1, -7, 1, -5, -6]), "expected ", [2, -4, 3, -9, 1, -1, -7, -5, -6]