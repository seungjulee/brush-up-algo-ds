# http://people.cs.clemson.edu/~bcdean/dp_practice/dp_1.swf
# Input: Array A[1, n] of real numbers
# S(j): max sum over all M(j)s
# M(j): max sum over all windows ending at j
# M(j) = max(M(j-1)+A[j], A[j])
# 
# O(n)
def solve_max_subsequence(arr):
    curr_sum = 0
    max_sum = 0

    curr_start_i = 0
    max_start_i = 0
    max_end_i = 0

    for i, v in enumerate(arr):
        if v < curr_sum + v:
            curr_sum += v
        else:
            curr_start_i = i
            curr_sum = v

        if max_sum < curr_sum:
            max_sum = curr_sum
            max_start_i = curr_start_i
            max_end_i = i

    return max_sum, arr[max_start_i:max_end_i+1]

def main(arr):
    print solve_max_subsequence(arr)

if __name__ == "__main__":
    arr = [1,2,-1,2,4,1,45,2,-40,7,5,19]
    main(arr)
