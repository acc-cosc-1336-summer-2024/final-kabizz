# stock.py

class Stock:
    def __init__(self, symbol, company_name, shares, purchase_price):
        self.__symbol = symbol
        self.__company_name = company_name
        self.__shares = shares
        self.__purchase_price = purchase_price

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name
    
    def get_shares(self):
        return self.__shares

    def get_purchase_price(self):
        return self.__purchase_price


def stock_purchase_history():
    # Create instances of Stock with purchase details
    apple_stock = Stock('AAPL', 'Apple Inc', 50, 150.00)
    caterpillar_stock = Stock('CAT', 'Caterpillar', 30, 200.00)
    kodak_stock = Stock('EK', 'Eastman Kodak', 20, 25.00)
    google_stock = Stock('GOOG', 'Google', 10, 1200.00)
    microsoft_stock = Stock('MSFT', 'Microsoft', 40, 300.00)
    
    # Add the stock instances to a dictionary
    stocks = {
        'AAPL': apple_stock,
        'CAT': caterpillar_stock,
        'EK': kodak_stock,
        'GOOG': google_stock,
        'MSFT': microsoft_stock
    }
    
    # Display the stock purchase history
    print(f"{'Symbol':<10} {'Company Name':<20} {'Shares':<10} {'Purchase Price':<15}")
    print("-" * 55)
    for symbol, stock in stocks.items():
        print(f"{stock.get_symbol():<10} {stock.get_company_name():<20} {stock.get_shares():<10} ${stock.get_purchase_price():<15.2f}")
