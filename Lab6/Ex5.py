age = 20
weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][1]
matinee = True

print(f"Age: {age}")
print(f"Weekday: {weekday}")
print(f"Matinee: {matinee}")

prices = []

prices.append(14)

if age >= 65:
    prices.append(8)

if weekday == "Tuesday":
    prices.append(10)

if matinee:
    if age >= 65:
        prices.append(5)
    else:
        prices.append(8)

price = min(prices)
print(f"Movie price: ${price}")
