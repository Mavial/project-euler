def distinct_power_count(start: int, stop: int) -> int:
    res = set()
    for a in range(start, stop + 1):
        for b in range(start, stop + 1):
            res.add(a**b)

    return len(res)

print(distinct_power_count(2, 100))