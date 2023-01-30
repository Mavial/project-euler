with open("p018_triangle_test.txt", "r") as file:
    triangle = tuple(tuple(int(n) for n in r.split(" ")) for r in file)


def path_sums(triangle, depth=0, width=0, total=0):
    if depth == len(triangle):
        return total
    res = []
    res.append(path_sums(triangle, depth + 1, width, total + triangle[depth][width]))
    res.append(
        path_sums(triangle, depth + 1, width + 1, total + triangle[depth][width])
    )
    return max(res)


print(path_sums(triangle))

# for p067 use .pop()