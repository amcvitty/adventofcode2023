debug = 1


def peek(x):
    debug and print(x)
    return x


def parse_round(round: str):
    ret = [0, 0, 0]
    cols = round.split(",")
    for col in cols:
        (n, c) = col.split()
        n = int(n)
        if c == "red":
            ret[0] = n
        elif c == "green":
            ret[1] = n
        elif c == "blue":
            ret[2] = n
    return ret


def parse_game(game: str):
    g, rounds = game.split(":")
    _, g = g.split()
    return int(g), [parse_round(r) for r in rounds.split(";")]


# combo and round are both 3-tuples [red, green, blue]
def round_possible(combo, round):
    return combo[0] >= round[0] and combo[1] >= round[1] and combo[2] >= round[2]


def max_round(combo, round):
    return [max(combo[0], round[0]), max(combo[1], round[1]), max(combo[2], round[2])]


def max_all(rounds):
    c2 = [0, 0, 0]
    for round in rounds:
        c2 = max_round(c2, round)
    return c2


def game_possible(combo, game_string: str):
    g, rounds = parse_game(game_string)
    if all([round_possible(combo, round) for round in rounds]):
        return g
    else:
        return 0


def min_possible(combo, game_string: str):
    g, rounds = parse_game(game_string)
