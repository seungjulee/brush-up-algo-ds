def count_binary_tree_with_N_nodes(N):
    memo = [0] * N
    def count_tree(N):
        if N <= 1:
            return 1
        else:
            combined = 0
            for i in xrange(1, N+1):
                if not memo[i-1]:
                    memo[i-1] = count_tree(i-1)
                left = memo[i-1]
                if not memo[N-i]:
                    memo[N-i] = count_tree(N-i)
                right = memo[N-i]
                combined += (left*right)
            return combined
    return count_tree(N)


def test_count_binary():

    print count_binary_tree_with_N_nodes(1) is 1
    print count_binary_tree_with_N_nodes(2) is 2
    print count_binary_tree_with_N_nodes(3) is 5

if __name__ == "__main__":
    test_count_binary()