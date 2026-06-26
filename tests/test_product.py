from src.axentx_product.product import Product

def test_product_creation():
    product = Product("Test Product", 10.99)
    assert product.get_name() == "Test Product"
    assert product.get_price() == 10.99
