#ask user to enter weight in pounds
#convert the weight to kilograms and return the value to the user
#name: chloe cornforth
#date: 09/05/2025

weight_in_pounds = input("Please enter your weight in pounds: ")
weight_in_kilograms = float(weight_in_pounds) * 0.453592
weight_in_kilograms_rounded = round(weight_in_kilograms)    

print(f"Your weight in {weight_in_kilograms_rounded} kilograms.")