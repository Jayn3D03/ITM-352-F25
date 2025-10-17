#Debugging exercise # 7
# Algorithm for multiplying two numbers

def multiply(x, y):
   product = x * y
   return product

first = input("Enter the first number: ")
second = input("Enter the second number: ")
prod = multiply(x=int(first), y=int(second))

print(f"The product of {first}, {second} is {prod}")
