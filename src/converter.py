def convert_currency(amount, from_rate, to_rate):
    if amount < 0:
        raise ValueError("Amount cannot be negative.")

    if from_rate <= 0:
        raise ValueError("Source currency rate must be positive.")

    if to_rate <= 0:
        raise ValueError("Target currency rate must be positive.")

    return amount * to_rate / from_rate