import os
import sqlite3

from database import initialize_database


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