def stock_tracker():
    stock_data = {
        'AAPL': {'price': 180, 'quantity': 5},
        'TSLA': {'price': 250, 'quantity': 2},
        'GOOG': {'price': 2000, 'quantity': 1}
    }

    total_investment = 0
    with open('portfolio.txt', 'w') as file:
        file.write("Stock\tQty\tPrice\tTotal\n")
        for stock, data in stock_data.items():
            total = data['price'] * data['quantity']
            total_investment += total
            file.write(f"{stock}\t{data['quantity']}\t{data['price']}\t{total}\n")
        file.write(f"\nTotal Investment: ${total_investment}")

    print("Portfolio saved to portfolio.txt")

stock_tracker()
