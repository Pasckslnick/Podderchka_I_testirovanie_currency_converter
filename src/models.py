from dataclasses import dataclass


@dataclass
class Operation:
    """
    Модель одной операции конвертации валют.
    """

    id: int | None = None
    date: str = ""
    from_currency: str = ""
    to_currency: str = ""
    amount: float = 0.0
    rate: float = 0.0
    result: float = 0.0