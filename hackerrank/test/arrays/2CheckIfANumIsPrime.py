def checkIfPrime(N):
    sieve = [1] * (N+1)

    sieve[0] = sieve[1] = 0

    for i in xrange(2, N+1):
        for j in xrange(i, N+1, i):
            if j == i:
                continue
            else:
                sieve[j] = 0

    if sieve[N] == 0:
        return False
    else:
        return True

def main():
    for N in raw_input():
        N = int(N)
        checkIfPrime(N)

main()