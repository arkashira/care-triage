from src.axentx_product.portfolio import Portfolio
from src.axentx_product.product import Product

def test_portfolio_creation():
    portfolio = Portfolio()
    assert portfolio.get_products() == []

def test_add_product_to_portfolio():
    portfolio = Portfolio()
    product = Product("Test Product", 10.99)
    portfolio.add_product(product)
    assert len(portfolio.get_products()) == 1
    assert portfolio.get_products()[0].get_name() == "Test Product"
    assert portfolio.get_products()[0].get_price() == 10.99
