import pytest

from app.main import get_human_age


@pytest.mark.parametrize("value1,value2,expected_results", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17])
])
def tests(value1: int, value2: int, expected_results: list) -> None:
    assert get_human_age(value1, value2) == expected_results


def test_negative() -> None:
    with pytest.raises(ValueError):
        get_human_age(-3, 0)


def test_not_integer() -> None:
    with pytest.raises(TypeError):
        get_human_age(3.43, 0)
