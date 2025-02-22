from typing import Any

import pandas as pd


def open_csv(file: str) -> Any:
    """
    Функция читает файл CSV и возвращает список словарей
    """
    data = pd.read_csv(file)
    return data.to_dict(orient="records")


def open_excel(file: str) -> Any:
    """
    Функция читает файл Excel и возвращает список словарей
    """
    data = pd.read_excel(file)
    return data.to_dict(orient="records")
