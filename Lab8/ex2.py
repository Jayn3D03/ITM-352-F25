import random

additional_requirements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Step 1: Pick a random element R1
R1 = random.choice(additional_requirements)

# Step 2: Remove R1 and pick R2
remaining_requirements = additional_requirements.copy()
remaining_requirements.remove(R1)
R2 = random.choice(remaining_requirements)

# Step 3: Assign R1, R2
assigned_requirements = [R1, R2]

print("Assigned additional requirements:", assigned_requirements)