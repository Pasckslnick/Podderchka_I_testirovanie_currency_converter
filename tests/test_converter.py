from src.converter import convert_currency


def test_convert_currency():
    result = convert_currency(
        amount=100,
        from_rate=1,
        to_rate=0.5
    )

    assert result == 50