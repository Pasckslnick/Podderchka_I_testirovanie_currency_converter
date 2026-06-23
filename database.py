import sqlite3


def initialize_database(db_name="currency_converter.db"):
    connection = sqlite3.connect(db_name)
    connection.close()