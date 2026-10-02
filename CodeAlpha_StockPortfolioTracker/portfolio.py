# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400,
    "AMZN": 180
}

portfolio = []
total_investment = 0

print("====================================")
print("      STOCK PORTFOLIO TRACKER")
print("====================================")

print("\nAvailable stocks:")
for stock in stock_prices:
    print(stock, "-", "$", stock_prices[stock])

while True:

    stock_name = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not available. Please choose from the available stocks.")
        continue

    quantity = int(input("Enter quantity: "))

    price = stock_prices[stock_name]
    investment = price * quantity

    portfolio.append((stock_name, quantity, price, investment))

    total_investment += investment

    print("Investment for", stock_name, ":", "$", investment)

print("\n====================================")
print("        PORTFOLIO SUMMARY")
print("====================================")

for stock, quantity, price, investment in portfolio:
    print(
        stock,
        "| Quantity:", quantity,
        "| Price: $", price,
        "| Investment: $", investment
    )

print("------------------------------------")
print("Total Investment: $", total_investment)

# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write("STOCK PORTFOLIO SUMMARY\n")
    file.write("========================\n")

    for stock, quantity, price, investment in portfolio:
        file.write(
            stock +
            " | Quantity: " + str(quantity) +
            " | Price: $" + str(price) +
            " | Investment: $" + str(investment) +
            "\n"
        )

    file.write("------------------------\n")
    file.write("Total Investment: $" + str(total_investment))

print("\nPortfolio saved successfully to portfolio.txt")