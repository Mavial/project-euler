# using factorial number system to find the 1.000.000th permutation

perm = list(range(10))


def factorial(n):
    """Function to calculate the factorial of a number"""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def factoradic(perm: list, n: int) -> list:
    """Function to find the factoradic representation of a number"""
    # Subtracting 1 from the given permutation number
    n = n - 1
    res = []
    # While there are still elements in the permutation list
    while len(perm) != 0:
        quot = n // factorial(len(perm) - 1)
        n = n % factorial(len(perm) - 1)

        res.append(perm.pop(quot))
    # returning the factoradic representation of the permutation
    return res


print("".join(str(x) for x in factoradic(perm, 1000000)))
