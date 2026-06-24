import pytest

from src.database import (
    add_currency,
    find_currency,
    update_currency,
    delete_currency,
)


def test_add_currency_via_database(tmp_path):
    file_path = tmp_path / "currencies.json"

    add_currency(file_path, "USD", 1.0)

    assert find_currency(file_path, "USD") == 1.0


def test_update_currency(tmp_path):
    file_path = tmp_path / "currencies.json"

    add_currency(file_path, "USD", 1.0)

    update_currency(file_path, "USD", 78.5)

    assert find_currency(file_path, "USD") == 78.5


def test_delete_currency(tmp_path):
    file_path = tmp_path / "currencies.json"

    add_currency(file_path, "USD", 1.0)

    delete_currency(file_path, "USD")

    with pytest.raises(ValueError):
        find_currency(file_path, "USD")


def test_find_currency(tmp_path):
    file_path = tmp_path / "currencies.json"

    add_currency(file_path, "EUR", 0.92)

    result = find_currency(file_path, "EUR")

    assert result == 0.92


def test_find_missing_currency(tmp_path):
    file_path = tmp_path / "currencies.json"

    with pytest.raises(ValueError):
        find_currency(file_path, "GBP")