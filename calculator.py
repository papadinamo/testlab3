def calculate_commission(amount: int) -> float:
    """
    Рассчитывает комиссию за денежный перевод.
    Args:
        amount (int): Сумма перевода от 100 до 50 000 руб.
    Returns:
        float: Размер комиссии в рублях.
    Raises:
        TypeError: Если сумма не является целым числом.
        ValueError: Если сумма выходит за допустимый диапазон.
    """
    if not isinstance(amount, int) or isinstance(amount, bool):
        raise TypeError("Сумма перевода должна быть целым числом.")
    if not 100 <= amount <= 50000:
        raise ValueError(
            "Сумма перевода должна быть от 100 до 50 000 руб."
        )
    if amount <= 1000:
        return 50.0
    if amount <= 20000:
        return 100.0
    if amount > 40000:
        return 500.0
    return 200.0 + amount * 0.01