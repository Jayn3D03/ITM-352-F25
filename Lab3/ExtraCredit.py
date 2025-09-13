from HandyMath import maximum, minimum, exponent, apply_function

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

a = number1
b = number2

print(apply_function(a, b, maximum))   
print(apply_function(a, b, minimum))   
print(apply_function(a, b, exponent))  