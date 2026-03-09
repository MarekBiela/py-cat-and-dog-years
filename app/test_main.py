from app.main import get_human_age


def test_0() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_0_upper_boundary() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_1_lower_boundary() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_1_upper_boundary() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_2_lower_boundary() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_regular_switch_point_1() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_regular_switch_point_2() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_random_value() -> None:
    assert get_human_age(100, 100) == [21, 17]
