#determind whether a list of purchases is within our budget
#name: Chloe Cornforth
#date: 10/01/2025

recent_purchases = [36.13, 23.87, 183.35, 22.93, 11.62]
budget = 50
total_spent = 0
for purchase in recent_purchases:
    total_spent += purchase

if total_spent > budget:
    print(f"You spent {total_spent: .2f} and that is over your budget of {budget: .2f}")
else:
    print(f"You are within your budget of {total_spent: .2f} and that is within your budget of {budget: .2f}")
