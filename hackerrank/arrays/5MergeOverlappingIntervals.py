
def merge_intervals(arr):
    range_arr = [[arr[0][0], arr[0][1]]]
    range_idx = 0
    MAX = 1
    MIN = 0
    for rang in arr[1:]:
        loc_min = rang[0]
        loc_max = rang[1]
        print range_arr, rang
        if loc_max > range_arr[-1][MAX] and loc_min < range_arr[-1][MAX]:
            range_arr[-1][MAX] = loc_max
        elif loc_min > range_arr[-1][MAX]:
            range_arr.append(rang)
    return range_arr

inpt_arr = [[1,3],[2,4],[5,7],[6,8]]
sorted_arr = sorted(inpt_arr, key= lambda l: l[1])
print merge_intervals(sorted_arr)