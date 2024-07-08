import pytest
from products import Product


def test_create_normal_product():
    """
    Test that creating a product with valid details works correctly.
    """
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active()


def test_create_product_invalid_details():
    """
    Test that creating a product with invalid details (empty name, negative price or quantity)
    raises a ValueError.
    """
    # Test with empty name
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)

    # Test with negative price
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)

    # Test with negative quantity
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=1450, quantity=-100)


def test_product_becomes_inactive_when_quantity_is_zero():
    """
    Test that a product becomes inactive when its quantity reaches zero.
    """
    product = Product("MacBook Air M2", price=1450, quantity=1)
    product.buy(1)
    assert not product.is_active()


def test_product_purchase_modifies_quantity_and_returns_right_output():
    """
    Test that purchasing a product modifies the quantity correctly and returns the right total price.
    """
    product = Product("MacBook Air M2", price=1450, quantity=100)
    total_price = product.buy(10)
    assert total_price == 14500
    assert product.quantity == 90


def test_buying_larger_quantity_than_exists_raises_exception():
    """
    Test that attempting to buy more quantity than available raises an exception.
    """
    product = Product("MacBook Air M2", price=1450, quantity=100)
    with pytest.raises(Exception):
        product.buy(101)
