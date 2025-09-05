#ask the user to enter a temperature in degrees Fahrenheit
#convert the temperature to degrees Celsius and return the value to the user
#name: chloe cornforth
#date: 09/05/2025

degreesF = input("Enter a temperature in degrees Fahrenheit: ")

degreesF_float = float(degreesF)
degreesC = (degreesF_float - 32) * 5.0/9.0
degreesC = round(degreesC)

print(f"{degreesF_float} degrees Fahrenheit is {degreesC} degrees Celsius.")    
