stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 300
}

total_investment = 0

print("=== Stock Portfolio Tracker ===")

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))

    investment = stock_prices[stock] * quantity
    total_investment += investment

    print(f"Investment in {stock}: ${investment}")

print("\nTotal Investment Value: $", total_investment)

with open("portfolio_summary.txt", "w") as file:
    file.write(f"Total Investment Value: ${total_investment}")

print("Summary saved to portfolio_summary.txt")