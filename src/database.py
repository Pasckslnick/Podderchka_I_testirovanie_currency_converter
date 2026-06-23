import sqlite3
from src.models import Operation
from pathlib import Path
import json

DATABASE_PATH = Path("data") / "currency_converter.db"






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

def add_operation(db_name: str, operation: Operation):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO operations(
            date,
            from_currency,
            to_currency,
            amount,
            rate,
            result
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            operation.date,
            operation.from_currency,
            operation.to_currency,
            operation.amount,
            operation.rate,
            operation.result,
        ),
    )

    connection.commit()
    connection.close()


def load_data(file_path):
    file_path = Path(file_path)

    if not file_path.exists():
        file_path.write_text("{}", encoding="utf-8")
        return {}

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
    
def save_data(file_path, data):
    file_path = Path(file_path)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def add_currency(file_path, currency, rate):
    data = load_data(file_path)

    if currency in data:
        raise ValueError("Currency already exists.")

    data[currency] = rate

    save_data(file_path, data)