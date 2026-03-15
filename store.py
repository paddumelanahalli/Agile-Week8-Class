#test_store.py
import pytest
from store import get_price

def test_missing_item_raises_error():
    with pytest.raises(KeyError):
        get_price("Banana")


def test_case_insensitivity():
    assert get_price("apple") == 1.50

#store.py
inventory = {"Apple": 1.50}

"""
def get_price(item):
    return inventory[item]
"""

def get_price(item):
    # Refactor: Normalize input to Title Case
    formatted_item = item.strip().capitalize()
    return inventory[formatted_item]
