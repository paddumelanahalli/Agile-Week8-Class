#Test_cart.py
import pytest
from cart_system import ShoppingCart
"""
# This is our Fixture. It "preps" a fresh cart for every test.
@pytest.fixture
def empty_cart():
    return ShoppingCart()

def test_add_item_updates_total(empty_cart):
    #    Notice we pass 'empty_cart' as an argument to the test!
    empty_cart.add_item("Laptop", 1000)
    assert empty_cart.total == 1000
    assert len(empty_cart.items) == 1

"""

@pytest.fixture
def persistent_cart():
    # SETUP: Create the cart and a temp file
    cart = ShoppingCart()
    print("\n[Setup] Creating temporary session...")

    yield cart # This is where the test happens!

    # TEARDOWN: This runs AFTER the test finishes
    print("[Teardown] Deleting temporary session...")
    cart.items = []
    cart.total = 0


#cart_system.py

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0

    def add_item(self, name, price):
        self.items.append(name)
        self.total += price
