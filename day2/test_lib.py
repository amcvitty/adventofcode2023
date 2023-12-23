from lib import *


def test_parse_game():
    assert parse_game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == (
        1,
        [
            [4, 0, 3],
            [1, 2, 6],
            [0, 2, 0],
        ],
    )


def test_parse_round():
    assert parse_round("3 blue, 4 red") == [4, 0, 3]
    assert parse_round("1 red, 2 green, 6 blue") == [1, 2, 6]


def test_round_possible():
    combo = [12, 13, 14]
    assert round_possible(combo, [4, 0, 3])
    # , [1, 2, 6], [0, 2, 0]]


def test_running_max():
    assert max_round([1, 2, 3], [3, 2, 1]) == [3, 2, 3]
