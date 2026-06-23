from src.menu import run_menu_command
from src.database import load_data
from src.database import update_currency

from src.converter import convert_currency
from src.database import delete_currency

def test_menu_add_currency(tmp_path):
    file_path = tmp_path / "currencies.json"

    result = run_menu_command(
        command="add",
        file_path=file_path,
        currency="USD",
        rate=1.0
    )

    data = load_data(file_path)

    assert data["USD"] == 1.0
    assert result == "Currency added"







def test_menu_update_currency(tmp_path):
    file_path = tmp_path / "currencies.json"

    run_menu_command("add", file_path, "USD", 1.0)

    result = run_menu_command(
        command="update",
        file_path=file_path,
        currency="USD",
        rate=78.5
    )

    data = load_data(file_path)

    assert data["USD"] == 78.5
    assert result == "Currency updated"






def test_menu_delete_currency(tmp_path):
    file_path = tmp_path / "currencies.json"

    run_menu_command("add", file_path, "USD", 1.0)

    result = run_menu_command(
        command="delete",
        file_path=file_path,
        currency="USD"
    )

    data = load_data(file_path)

    assert "USD" not in data
    assert result == "Currency deleted"





def test_menu_convert():
    result = run_menu_command(
        command="convert",
        amount=100,
        from_rate=1,
        to_rate=0.5
    )

    assert result == 50