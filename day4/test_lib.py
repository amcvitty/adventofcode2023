from lib import *


def test_find_numbers():
    assert find_numbers("........") == []
    assert find_numbers(".35....") == [(35, 1, 2)]
    assert find_numbers(".35...234.") == [(35, 1, 2), (234, 6, 8)]


def test_find_surrounding_coords():
    assert find_surrounding_coords(1, 1, 2) == [
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 0),
        (1, 3),
        (2, 0),
        (2, 1),
        (2, 2),
        (2, 3),
    ]
