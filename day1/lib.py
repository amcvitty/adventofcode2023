def to_int(x):
    return 1


def get_ints(str):
    return list(filter(None, [get_int(str, i) for (i) in range(0, len(str))]))


def starts_with(str, prefix):
    return str[0 : len(prefix)] == prefix


def get_int(str, i):
    x = str[i]
    try:
        if int(x) > 0:
            return int(x)
    except:
        pass
    rem = str[i:-1]
    if starts_with(rem, "one"):
        return 1
    if starts_with(rem, "two"):
        return 2
    if starts_with(rem, "three"):
        return 3
    if starts_with(rem, "four"):
        return 4
    if starts_with(rem, "five"):
        return 5
    if starts_with(rem, "six"):
        return 6
    if starts_with(rem, "seven"):
        return 7
    if starts_with(rem, "eight"):
        return 8
    if starts_with(rem, "nine"):
        return 9
