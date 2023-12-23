from lib import *


def test_get_ints():
    assert get_ints("123") == [1, 2, 3]


def test_starts_with():
    assert starts_with("dave", "da")
    assert not starts_with("d", "da")


def test_get_int():
    assert get_int("1234", 0) == 1
    assert get_int("1234", 2) == 3
    assert get_int("astwonesd", 2) == 2
    assert get_int("astwonesd", 4) == 1
