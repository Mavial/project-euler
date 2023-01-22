# calculate the nth Fibonacci number and the index
# at which the first 1000-digit Fibonacci number appears

n, p, i = 1, 1, 2

while len(str(n)) != 1000:
    n, p = n + p, n
    i += 1

print(i)
