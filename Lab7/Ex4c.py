recent_purchases = [36.13, 23.87, 183.35, 22.93, 11.62]
budget = 50

def budget_check(purchases, budget):
    total_spent = sum(purchases)
    if total_spent > budget:
        print(f"You spent ${total_spent:.2f} and that is over your budget of ${budget:.2f}")
    else:
        print(f"You are within your budget of ${total_spent:.2f} and that is within your budget of ${budget:.2f}")

budget_check(recent_purchases, budget)

# test cases
def test_check_budget():
    assert budget_check([36.13, 23.87, 183.35, 22.93, 11.62], 50) == \
        "You spent 277.90 and that is over your budget of 50.00"
    assert budget_check([10, 20, 15], 50) == \
        "You are within your budget of 45.00 and that is within your budget of 50.00"
    assert budget_check([], 50) == \
        "You are within your budget of 0.00 and that is within your budget of 50.00"
    assert budget_check ([25, 25], 50) == \
        "You are within your budget of 50.00 and that is within your budget of 50.00"
    assert budget_check([60], 50) == \
        "You spent 60.00 and that is over your budget of 50.00"

test_check_budget()