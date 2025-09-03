#Ask the user to enter a number between 1 and 100. Square the number 
#Square the number and print the result
#Name: Chloe Cornforth
#Date: 09/03/2025

value_entered = input("Please enter an floating point number between 1 and 100: ")
print("The user entered", value_entered)
value_as_float = float(value_entered)

value_squared = value_as_float**2
print(f"The value squared is ", value_squared)