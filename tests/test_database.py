import os
import sqlite3
import pytest

from src.database import (
    initialize_database,
    add_operation
)
from src.models import Operation
import json
from src.database import save_data
from src.database import add_currency, load_data
from src.database import update_currency



def test_database_is_created():
    db_name = "test_currency.db"

    if os.path.exists(db_name):
        os.remove(db_name)

    initialize_database(db_name)

    assert os.path.exists(db_name)

    os.remove(db_name)


def test_operations_table_exists():
    db_name = "test_currency.db"

    if os.path.exists(db_name):
        os.remove(db_name)

    initialize_database(db_name)

    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        AND name='operations'
    """)

    table = cursor.fetchone()

    connection.close()
    os.remove(db_name)

    assert table is not None



def test_add_operation():
    db_name = "test_currency.db"

    if os.path.exists(db_name):
        os.remove(db_name)

    initialize_database(db_name)

    operation = Operation(
        date="2026-06-23",
        from_currency="USD",
        to_currency="RUB",
        amount=100,
        rate=78.5,
        result=7850,
    )

    add_operation(db_name, operation)

    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM operations")

    operation = cursor.fetchone()



    connection.close()
    os.remove(db_name)

    assert operation is not None
    assert operation[2] == "USD"
    assert operation[3] == "RUB"
    assert operation[4] == 100
    assert operation[5] == 78.5
    assert operation[6] == 7850



def test_load_creates_empty_database(tmp_path):
    file_path = tmp_path / "currencies.json"

    data = load_data(file_path)

    assert data == {}
    assert os.path.exists(file_path)



def test_save_data(tmp_path):
    file_path = tmp_path / "currencies.json"

    data = {
        "USD": 1.0,
        "EUR": 0.92,
        "RUB": 78.5
    }

    save_data(file_path, data)

    with open(file_path, "r", encoding="utf-8") as file:
        saved_data = json.load(file)

    assert saved_data == data


def test_add_currency(tmp_path):
    file_path = tmp_path / "currencies.json"

    add_currency(file_path, "USD", 1.0)

    data = load_data(file_path)

    assert data["USD"] == 1.0


def test_add_existing_currency(tmp_path):
    file_path = tmp_path / "currencies.json"

    add_currency(file_path, "USD", 1.0)

    with pytest.raises(ValueError):
        add_currency(file_path, "USD", 1.2)


from src.database import update_currency


def test_update_currency(tmp_path):
    file_path = tmp_path / "currencies.json"

    add_currency(file_path, "USD", 1.0)

    update_currency(file_path, "USD", 78.5)

    data = load_data(file_path)

    assert data["USD"] == 78.5



def test_update_missing_currency(tmp_path):
    file_path = tmp_path / "currencies.json"

    with pytest.raises(ValueError):
        update_currency(file_path, "USD", 80)