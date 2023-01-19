def sum_proper_divisors(n):
    divisors = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sum(divisors) - n

abundant_numbers = []

for i in range(12, 28112):
    if sum_proper_divisors(i) > i:
        abundant_numbers.append(i)

print(len(abundant_numbers))