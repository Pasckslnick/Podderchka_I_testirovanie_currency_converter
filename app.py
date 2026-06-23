from pathlib import Path
import sys
sys.stdout.reconfigure(encoding='utf-8')

from src.database import (
    add_currency,
    update_currency,
    delete_currency,
    find_currency,
    load_data,
)
from src.converter import convert_currency

DATA_FILE = Path("data/currencies.json")


def print_menu():
    print("\n========== Currency Converter ==========")
    print("1. Показать валюты")
    print("2. Добавить валюту")
    print("3. Обновить валюту")
    print("4. Удалить валюту")
    print("5. Найти валюту")
    print("6. Конвертировать валюту")
    print("0. Выход")
    print("========================================")


def show_currencies():
    data = load_data(DATA_FILE)

    if not data:
        print("\nNo currencies found.")
        return

    print("\nCurrencies:")

    for currency, rate in data.items():
        print(f"{currency} : {rate}")


def add():
    currency = input("Currency code: ").upper()
    rate = float(input("Rate: "))

    add_currency(DATA_FILE, currency, rate)

    print("Currency added.")


def update():
    currency = input("Currency code: ").upper()
    rate = float(input("New rate: "))

    update_currency(DATA_FILE, currency, rate)

    print("Currency updated.")


def delete():
    currency = input("Currency code: ").upper()

    delete_currency(DATA_FILE, currency)

    print("Currency deleted.")


def find():
    currency = input("Currency code: ").upper()

    rate = find_currency(DATA_FILE, currency)

    print(f"{currency} = {rate}")


def convert():
    from_currency = input("From: ").upper()
    to_currency = input("To: ").upper()

    amount = float(input("Amount: "))

    from_rate = find_currency(DATA_FILE, from_currency)
    to_rate = find_currency(DATA_FILE, to_currency)

    result = convert_currency(amount, from_rate, to_rate)

    print(f"\nResult: {amount} {from_currency} = {result:.2f} {to_currency}")


def main():
    while True:
        print_menu()

        choice = input("Choose: ")

        try:
            if choice == "1":
                show_currencies()

            elif choice == "2":
                add()

            elif choice == "3":
                update()

            elif choice == "4":
                delete()

            elif choice == "5":
                find()

            elif choice == "6":
                convert()

            elif choice == "0":
                print("Goodbye!")
                break

            else:
                print("Unknown command.")

        except ValueError as error:
            print(f"Error: {error}")

        except Exception as error:
            print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()