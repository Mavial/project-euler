n, fact = 100, 1
for i in range(1, n + 1): fact *= i
print(sum([int(i) for i in str(fact)]))
