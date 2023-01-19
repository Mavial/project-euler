res = 0
n, p = 2, 1
while n <= 4000000 or p <= 4000000:
    n, p = n+p, n
    if n % 2 == 0: res += n
print(res)