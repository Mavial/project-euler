def digit_fifth_powers(n):
    res = 0
    for i in range(2, n):
        if i == sum(tuple(int(d)**5 for d in str(i))):
            res += i
    return res

print(digit_fifth_powers(200000))