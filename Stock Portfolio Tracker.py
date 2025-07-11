stock_prices = {
    "APPLE": 180,
    "TESLA": 250,
    "GOOGLE": 190,
    "AMAZON": 160,
    "BMW": 120
}

total_investment = 0

print("Welcome to the Stock Calculator📈!")

while True:
    stock = input("Which stock do you want to add? Type 'done' to stop: ").upper()
    
    if stock == "DONE":
        break
    
    if stock in stock_prices:
        quantity = int(input(f"Enter the quantity of {stock}: "))
        total_investment += stock_prices[stock] * quantity
    else:
        print("Stock not found in list.")

print("Your total investment is 💰", total_investment)
print("Thanks for using the stock calculator📊!")
