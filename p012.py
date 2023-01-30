from math import sqrt


def tri_num_gen(n: int) -> int:
    return n * (n + 1) // 2

# prime factoring
def factor_count(n: int) -> int:
    prime_factors = 0
    for p in range(1, int(sqrt(n)) + 1):
        if n % p == 0:
            prime_factors += 2
    return prime_factors


n, res = 2, 0
while res <= 500:
    tri_num = tri_num_gen(n)
    res = factor_count(tri_num)
    n += 1

print(tri_num)
