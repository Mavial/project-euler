with open("p013_list.txt", "r") as n_list:
    res = [int(line) for line in n_list]

print(sum(res))