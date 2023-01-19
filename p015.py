# source: https://stemhash.com/counting-lattice-paths/


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def binom_coeff(n: int, k: int) -> int:
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

# (k+n, n) -> (20+20, 20)
print(binom_coeff(40, 20))
