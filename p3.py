def is_prime(n):
    if n <= 1: return False
    if n <= 3: return True
    if (n % 2 == 0 or n % 3 == 0): return False
    for i in range(5, n, 6):
        if ( n % i == 0 or n % (i+2) == 0): return False
    return True
i = 2
while True:
    if not 600851475143 % i == 0: i += 1
    else:
        if is_prime(int(600851475143/i)): break
        else: i += 1

print(int(600851475143/i))