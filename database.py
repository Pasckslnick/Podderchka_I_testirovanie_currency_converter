import sqlite3


def initialize_database(db_name="currency_converter.db"):
    connection = sqlite3.connect(db_name)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS operations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            from_currency TEXT NOT NULL,
            to_currency TEXT NOT NULL,
            amount REAL NOT NULL,
            rate REAL NOT NULL,
            result REAL NOT NULL
        )
    """)

    connection.commit()
    connection.close()