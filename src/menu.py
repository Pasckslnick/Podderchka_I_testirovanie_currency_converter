from src.database import (
    add_currency,
    update_currency,
    delete_currency
    
)

from src.converter import convert_currency

def run_menu_command(command, **kwargs):
    if command == "add":
        return "Currency added"

    if command == "update":
        return "Currency updated"

    if command == "delete":
        return "Currency deleted"

    if command == "convert":
        return convert_currency(
            kwargs["amount"],
            kwargs["from_rate"],
            kwargs["to_rate"]
        )

    raise ValueError("Unknown command")