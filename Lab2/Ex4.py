#ask the user to enter a floating point number between 1 and 100
#square the number and return the value to the user , rounded to 2 decimal points
#name : chloe cornforth
#date: 09/05/2025

value_entered = input("Please enter a floating point number between 1 and 100: ")
value_entered_float = float(value_entered)
squared_value = value_entered_float **2
rounded_value = round(squared_value, 2)

print(f"The square of {value_entered} is {rounded_value}")
print(f"The value without rounding is {squared_value}")