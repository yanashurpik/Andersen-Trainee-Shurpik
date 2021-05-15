import pytest
from fun1 import first_function
from fun2 import second_function
from fun3 import third_function


@pytest.mark.parametrize("first_data, expected_result", [
    (9, True),
    (8, True),
    (11, True),
    (5, False),
])
def test_first_function(first_data, expected_result):
    assert first_function(first_data) == expected_result


@pytest.mark.parametrize("second_data, expected_result", [
    ("Вячеслав", True),
    ("Аня", False),
])
def test_second_function(second_data, expected_result):
    assert second_function(second_data) == expected_result


def test_third_function():
    assert third_function([12, 3, 9, 6]) == [12, 3, 9, 6]
    assert third_function([]) == []
    assert third_function([5, 6]) == [6]


