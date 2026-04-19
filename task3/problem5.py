def calculate_bill(prices , items_bought):
    total=0
    for item in items_bought:
        total+=prices[item]
    return total
prices = {"apple": 0.5, "banana": 0.3}
items_bought = ["apple", "banana", "apple"]

total = calculate_bill(prices, items_bought)
print(total)
 