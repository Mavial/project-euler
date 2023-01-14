def proper_divisor_sum(n):
    filtered = [x for x in list(range(1, n)) if n % x == 0]
    return sum(filtered)

sums, amicable = [], []

for i in range(1, 10000):
    i_div_sum = proper_divisor_sum(i)
    if i in sums and i == proper_divisor_sum(i_div_sum):
            amicable.append(i)
            amicable.append(i_div_sum)
    sums.append(proper_divisor_sum(i))

print(sum(amicable))

# not optimized