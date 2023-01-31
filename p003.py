num = 600851475143


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i**2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


i = 2
while True:
    if not num % i == 0:
        i += 1
    else:
        if is_prime(int(num / i)):
            break
        else:
            i += 1

print(int(num / i))

# not very proud of this.
