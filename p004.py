def is_palindrome(n):
    if n == int(str(n)[::-1]): return True
    return False

largest_palindrome = 0
for a in range(999):
    for b in range(999):
        if is_palindrome(a*b) and a*b > largest_palindrome: largest_palindrome = a*b

print(largest_palindrome)
