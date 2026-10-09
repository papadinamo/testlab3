import pytest
from calculator import calculate_commission


@pytest.mark.parametrize("amount, expected", [
    (100, 50.0),
    (1000, 50.0),
    (1001, 100.0),
    (20000, 100.0),
    (20001, 400.01),
    (40000, 600.0),
    (40001, 500.0),
    (50000, 500.0),
])
def test_commission(amount, expected):
    assert calculate_commission(amount) == expected


@pytest.mark.parametrize("amount", [99, 50001, -1])
def test_invalid_amount(amount):
    with pytest.raises(ValueError):
        calculate_commission(amount)


@pytest.mark.parametrize("amount", [100.5, "1000", None, True])
def test_invalid_type(amount):
    with pytest.raises(TypeError):
        calculate_commission(amount)