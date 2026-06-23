from src.converter import convert_currency
import pytest


def test_convert_currency():
    result = convert_currency(
        amount=100,
        from_rate=1,
        to_rate=0.5
    )

    assert result == 50


def test_convert_negative_amount():
    with pytest.raises(ValueError):
        convert_currency(
            amount=-100,
            from_rate=1,
            to_rate=0.9
        )

def test_convert_zero_from_rate():
    with pytest.raises(ValueError):
        convert_currency(
            amount=100,
            from_rate=0,
            to_rate=1
        )

def test_convert_zero_to_rate():
    with pytest.raises(ValueError):
        convert_currency(
            amount=100,
            from_rate=1,
            to_rate=0
        )