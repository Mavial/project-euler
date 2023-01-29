# solved by chatGPT and other AIs

from math import gcd

def longest_recurring_cycle(n):
    max_length = 0
    d_with_max_length = 0
    for d in range(2, n):
        if gcd(d, 10) == 1:
            length = 1
            while (10 ** length - 1) % d != 0:
                length += 1
            if length > max_length:
                max_length = length
                d_with_max_length = d
    return d_with_max_length

print(longest_recurring_cycle(1000))
