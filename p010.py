def prime_sum(n: int) -> int:
    p = 2
    sieve = list(range(2, n))
    while p * p < n:
        sieve = [x for x in sieve if x == p or x % p != 0]
        p = sieve[sieve.index(p) + 1]
    return sum(sieve)

print(prime_sum(2000000))