debug = 1


def peek(x):
    debug and print(x)
    return x


# Finds numbers in the string returning list of 3-tuples(number, start, end)
# String must start and end with a .
def find_numbers(line: str):
    ret = []
    found_num = False
    start = 0
    for i in range(0, len(line)):
        if found_num:
            if not line[i].isdigit():
                ret.append((int(line[start:i]), start, i - 1))
                found_num = False
        else:
            if line[i].isdigit():
                start = i
                found_num = True
    return ret


def find_surrounding_coords(i, j1, j2):
    return (
        [(i - 1, j) for j in range(j1 - 1, j2 + 2)]
        + [(i, j1 - 1), (i, j2 + 1)]
        + [(i + 1, j) for j in range(j1 - 1, j2 + 2)]
    )


def is_symbol(grid, i, j):
    x = grid[i][j]
    return (not x.isdigit()) and (not x == ".")


def n_contains(number, i, j):
    _, i2, j1, j2 = number
    return i == i2 and j1 <= j and j2 >= j
