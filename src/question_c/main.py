from question_c import Stock

def main():
    # Creating instances of Stock class
    apple = Stock('AAPL', 'Apple Inc')
    caterpillar = Stock('CAT', 'Caterpillar')
    kodak = Stock('EK', 'Eastman Kodak')
    google = Stock('GOOG', 'Google')
    microsoft = Stock('MSFT', 'Microsoft')
    
    # List of all stock objects
    stocks = [apple, caterpillar, kodak, google, microsoft]
    
    # Display the stock report header
    print("Stock Report\n")
    print(f"{'Company Name':<20} {'Symbol':<10}")
    print("=" * 30)  # Line separator
    
    # Displaying the symbol and company name for each stock
    for stock in stocks:
        print(f"{stock.get_company_name():<20} {stock.get_symbol():<10}")

if __name__ == "__main__":
    main()