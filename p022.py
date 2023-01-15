def sort(names_list: list[str]):
    if len(names_list) <= 1:
        return names_list
    pivot = names_list[0]
    left = [x for x in names_list if x < pivot]
    middle = [x for x in names_list if x == pivot]
    right = [x for x in names_list if x > pivot]
    return sort(left) + middle + sort(right)

with open("p022_names.txt", "r") as f:
    names = f.read()
    names_list = names.replace('"', "").split(",")
    sorted_names = sort(names_list)


result = sum(
    [
        sum([ord(c) - ord("A") + 1 for c in name]) * (sorted_names.index(name) + 1)
        for name in sorted_names
    ]
)
print(result)
