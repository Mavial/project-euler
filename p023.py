# Define a function to calculate the sum of proper divisors
def sum_proper_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sum(divisors) - n

# Create a list of abundant numbers
abundant_numbers = []
for i in range(12, 28112):
    if sum_proper_divisors(i) > i:
        abundant_numbers.append(i)

# Create a sieve of all numbers up to 28123 as a set
sieve = set(range(28124))

# Remove all numbers that can be written as the sum of two abundant numbers
for i1, val1 in enumerate(abundant_numbers):
    for i2 in range(i1, len(abundant_numbers)):
        sum_of_abundant_nums = val1 + abundant_numbers[i2]
        if sum_of_abundant_nums in sieve:
            sieve.remove(sum_of_abundant_nums)

# Print the final answer
print(sum(sieve))
