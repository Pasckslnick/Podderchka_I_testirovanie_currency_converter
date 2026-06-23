import os

from database import initialize_database


def test_database_is_created():
    db_name = "test_currency.db"

    if os.path.exists(db_name):
        os.remove(db_name)

    initialize_database(db_name)

    assert os.path.exists(db_name)

    os.remove(db_name)