# type: ignore

word_len_dict = {
    "1": 3,
    "2": 3,
    "3": 5,
    "4": 4,
    "5": 4,
    "6": 3,
    "7": 5,
    "8": 5,
    "9": 4,
    "10": 3,
    "11": 6,
    "12": 6,
    "13": 8,
    "14": 8,
    "15": 7,
    "16": 7,
    "17": 9,
    "18": 8,
    "19": 8,
    "xx": {
        "2": 6,
        "3": 6,
        "4": 5,
        "5": 5,
        "6": 5,
        "7": 7,
        "8": 6,
        "9": 6,
    },
    "xxx": 7,
    "xxxx": 8,
    "and": 3,
}

total = 0
for i in range(1, 1001):
    w_len = 0
    i_str = str(i)[::-1]

    if i < 20:
        w_len = word_len_dict[i_str[::-1]]
    else:
        if i == 1000:
            w_len += word_len_dict["1"] + word_len_dict["xxxx"]
        if len(i_str) > 2 and i_str[2] != "0":
            w_len += word_len_dict[i_str[2]] + word_len_dict["xxx"]
            if i_str[0] + i_str[1] != "00":
                w_len += word_len_dict["and"]
        if int(i_str[1] + i_str[0]) < 20 and int(i_str[1] + i_str[0]) > 0:
            w_len += word_len_dict[str(int(i_str[1] + i_str[0]))]
        else:
            if i_str[1] != "0":
                w_len += word_len_dict["xx"][i_str[1]]
            if i_str[0] != "0":
                w_len += word_len_dict[i_str[0]]

    total += w_len

print(total)
