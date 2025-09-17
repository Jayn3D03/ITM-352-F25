# test to see how the functions defined in handy math work
# name: chloecornforth
# date: 9/12/2025

import HandyMath

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

mid = HandyMath.midpoint(number1, number2)
print(f"The midpoint between {number1} and {number2} is {mid}")

exp = HandyMath.exponent(number1, number2)
print(f"{number1} raised to the power of {number2} is {exp}")

max_num = HandyMath.maximum(number1, number2)
print(f"The maximum of {number1} and {number2} is {max_num}")

min_num = HandyMath.minimum(number1, number2)
print(f"The minimum of {number1} and {number2} is {min_num}")

sq_root = HandyMath.square_root(number1)
print(f"The square root of {number1} is {sq_root}")
