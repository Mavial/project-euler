from math import ceil

def sum_of_corners(grid_size):
    increment = 20
    res = 1
    ring_val = 4
    for _ in range(1, ceil(grid_size / 2)):
        ring_val += increment
        increment += 32
        res += ring_val
    return res

print(sum_of_corners(1001))