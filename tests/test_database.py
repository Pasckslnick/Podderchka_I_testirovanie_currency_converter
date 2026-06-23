import os
import sqlite3

from database import (
    initialize_database,
    add_operation
)

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

    add_operation(
        db_name=db_name,
        date="2026-06-23 18:00",
        from_currency="USD",
        to_currency="RUB",
        amount=100,
        rate=78.5,
        result=7850
    )

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